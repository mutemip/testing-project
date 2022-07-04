from rest_framework import generics, status
from rest_framework.response import Response


from booking_manager_api.models import EntityWorkingDays,EntityService,BookableService,EntityBookingSchedule

from intel_api.views.authentication import GetRequestAuthenticationBase
from datetime import datetime
from booking_manager_api.models.util import get_object_or_none
from rest_framework.views import APIView
from clients_booking_api.serializers import UserBookServiceSerializer

from clients_booking_api.models import UserBookService
from clients_booking_api.serializers import ManagerUserBookServiceSerializer

from clients_booking_api.models import UserBookTravelInformation
# from clients_booking_api.tasks import send_booking_info_to_country
from datetime import date

DATE_FORMAT="%d-%m-%Y"
TODAY = date.today()

class PossibleBookingTimeSlots(GetRequestAuthenticationBase,generics.ListAPIView):
    """
        localhost:8000/api/v1/booking/client/possible/bookings/{service_id}/{bookind date(format dd-mm-yyyy 01-10-2021)}/ 

        eg:
            localhost:8000/api/v1/booking/client/possible/bookings/2/01-10-2021/
        Headers:
            "session-key": "KvZsBSCAah",
            "Authorization": "Token ca479c930b178ef983144e6e167ea14985cec1d3"


        Response:
            {
              "status": "success",
              "data": [
                {
                  "entity_schedule_id": 25,
                  "time_slot": {
                    "start_time": "00:00:00",
                    "end_time": "01:00:00"
                  }
                },
                {
                  "entity_schedule_id": 26,
                  "time_slot": {
                    "start_time": "01:00:00",
                    "end_time": "02:00:00"
                  }
                },
                {
                  "entity_schedule_id": 27,
                  "time_slot": {
                    "start_time": "02:00:00",
                    "end_time": "03:00:00"
                  }
                }
              ]
            }
    """
    def serialize_data(self,schedules):
        data = list()
        for schedule in schedules:
            d=dict()
            time_slot = schedule.timeslot
            d["entity_schedule_id"] = schedule.id
            d['time_slot'] = {"start_time":str(time_slot.start_time),"end_time":time_slot.end_time}
            data.append(d)
        return data

    def list(self, request,**kwargs):
        try:
            user = self.authenticate(request)
        except Exception as e:
            return Response({"status":"error","message":"%s"%str(e)},status=status.HTTP_401_UNAUTHORIZED) 

        service_id = kwargs.get('service_id',None)
        booking_date = kwargs.get("booking_date",None)
        # check past date
        try:
            if service_id and booking_date:
                date = datetime.strptime(booking_date, DATE_FORMAT)
                if date.date() < TODAY:
                    raise Exception("Date cannot be in the past.")
                entity_service = get_object_or_none(EntityService,id=service_id)
                entity_working_day = get_object_or_none(EntityWorkingDays,day=date.isoweekday(),active=True)

                if entity_service and entity_working_day:
                    entity_schedule_for_the_day = EntityBookingSchedule.get_active_schedules(day=entity_working_day,date=date,entity_service=entity_service)
                    return Response({"status": "success", "data": self.serialize_data(entity_schedule_for_the_day)},status=status.HTTP_200_OK)
                
                return Response({"status":"error","message":"Entity Service or working days not found."},status=status.HTTP_404_NOT_FOUND)  
            else:
                return Response({"status":"error","message":"Service id and date required."},status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"status":"error","message":"%s"%str(e)},status=status.HTTP_400_BAD_REQUEST)   


class CreateBooking(GetRequestAuthenticationBase,generics.CreateAPIView):
    serializer_class = UserBookServiceSerializer
    output_serializer = ManagerUserBookServiceSerializer
    def serialized(self,data):
        service = data.booked_entity_service
        external_entity = data.booked_entity_service.bookable_entity.detail
        s_data = {
            "booked_lab_name": external_entity.name,
            "service_name": service.service_name,
            "test": service.service.detail().name,
            "price": str(service.price)
        }
        schedule_data = data.entity_booking_schedule
        schedule_dict = {
            "day": schedule_data.entity_working_days.day.day,
            "maximum_bookee": schedule_data.maximum_bookee,
            "time_slot": "{} - {}".format(schedule_data.timeslot.start_time,schedule_data.timeslot.end_time)
        }
        ret_data = {
            "id": data.id,
            "created_at": data.created_at,
            "booked_by":data.booked_by.username,
            "service":s_data,
            "date":str(data.schedule_date),
            "booking_schedule":schedule_dict,
            "code":data.code,
            "payed":data.payed
        }
        travel_info = get_object_or_none(UserBookTravelInformation,userbookservice=data)
        if travel_info:
            ret_data['travel_info'] ={
                "travel_date":travel_info.travel_date,
                "departure_country":travel_info.departure_country,
                "arrival_country":travel_info.arrival_country,
                "passport_number":travel_info.passport_number,
                "transport_operator":travel_info.transport_operator
            } 
        return ret_data

    def serialized_data_2_country(self,data):
        schedule_data = data.entity_booking_schedule
        user = data.booked_by.user_profile()
        external_entity = data.booked_entity_service.bookable_entity.detail

        dd = {
            "first_name": user.first_name,
            "last_name": user.last_name,
            "email": user.email,
            "phone_number": user.phone_number,
            "booked_lab_name": external_entity.name,
            "booked_lab_country": external_entity.country,
            "booked_lab_proprietary_code": external_entity.proprietary_code,
            "booking_code": data.code,
            "booked_date": str(data.created_at),
            "booked_timeslot": "{} - {}".format(schedule_data.timeslot.start_time,schedule_data.timeslot.end_time),

        }
        travel_info = get_object_or_none(UserBookTravelInformation,userbookservice=data)
        if travel_info:
            dd["departure_country"] = travel_info.departure_country
            dd["arrival_country"] = travel_info.arrival_country
            dd["passport_number"] = travel_info.passport_number
            dd["transport_operator"] = travel_info.transport_operator
        return dd



    def post(self, request):
        try:
            user = self.authenticate(request)
        except Exception as e:
            return Response({"status":"error","message":"%s"%str(e)},status=status.HTTP_401_UNAUTHORIZED) 

        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            try:
                data = serializer.save(user=user)
            except Exception as e:
                return Response({
                    "status": "error",
                    "message": e.detail if hasattr(e, "detail") else str(e)},
                    status=status.HTTP_404_NOT_FOUND)
            # p_data = self.serialized_data_2_country(data)
            # send_booking_info_to_country.delay(userbookservice_id=data.id,data=p_data)
            return Response({"status": "success", "data": self.output_serializer(data).data},status=status.HTTP_200_OK)
            # return Response({"status": "success", "data": self.output_serializer(data).data},status=status.HTTP_200_OK)
        else:
            # return Response({"status":"error","message":"Error occured, please check data supplied."},status=status.HTTP_404_NOT_FOUND)
            return Response({"status":"error","message":serializer.errors},status=status.HTTP_400_BAD_REQUEST)


class ListPatientBookedServiceView(GetRequestAuthenticationBase,APIView):
    """
    Format:
        import requests

        url = "http://localhost:8000/api/v1/booking/client/list/services/booked/"

        payload = ""
        headers = {
            "session-key": "p",
            "Authorization": "Token ccf4a6cd8713c3eac13a4dd96db84e6c7c909581"
        }

        response = requests.request("GET", url, data=payload, headers=headers)

        print(response.text)
        
    Response:
        {
          "status": "success",
          "data": [
            {
              "booked_by": "knfonin@gmail.com",
              "booked_entity_service": 15,
              "schedule_date": "2021-10-02",
              "entity_booking_schedule": 30,
              "code": "",
              "payed": false
            },
            {
              "booked_by": "knfonin@gmail.com",
              "booked_entity_service": 16,
              "schedule_date": "2021-10-04",
              "entity_booking_schedule": 30,
              "code": "",
              "payed": false
            },...
          ]
        }
"""
    serializer_class = ManagerUserBookServiceSerializer

    def get(self,request):
        try:
            user = self.authenticate(request)
        except Exception as e:
            return Response({"status":"error","message":"%s"%str(e)},status=status.HTTP_401_UNAUTHORIZED) 

        try:
            user_entity = user.user_entity
            if user_entity:
                booked_services = UserBookService.get_patient_bookings(user_entity)
                return Response({"status":"success","data":self.serializer_class(booked_services,many=True).data},status=status.HTTP_200_OK)
            else:
                return Response({"status":"error","message":"Unauthorized user access."},status=status.HTTP_401_UNAUTHORIZED)
        except Exception as e:
            return Response({"status":"error","message":"Error occured(%s)"%str(e)},status=status.HTTP_400_BAD_REQUEST)
            




class GetUserBookServiceView(GetRequestAuthenticationBase,APIView):
    """
    Format:
        import requests

        url = "localhost:8000/api/v1/booking/client/get/user/book/service/3/"

        payload = ""
        headers = {
            "session-key": "wefdferdfef",
            "Authorization": "Token 6217dacf9501018d97819052f0bd3ee20df94b86"
        }

        response = requests.request("GET", url, data=payload, headers=headers)

        print(response.text)
    Response:
        {
          "status": "success",
          "data": 
            {
              "id": 3,
              "created_at": "2021-10-15T11:11:13.784406Z",
              "booked_by": "knfonin@gmail.com",
              "booked_entity_service": {
                "service": "Corona Virus Disease- 2019 (COVID-19)",
                "price": "$53.00"
              },
              "schedule_date": "2021-10-20",
              "entity_booking_schedule": {
                "working day": "Monday",
                "time_slot": "01:00:00 - 02:00:00",
                "max_bookee": 120
              },
              "code": "BO68713495",
              "payed": false
            }
        }    
    """
    serializer_class = ManagerUserBookServiceSerializer

    def get(self,request,**kwargs):
        try:
            user = self.authenticate(request)
        except Exception as e:
            return Response({"status":"error","message":"%s"%str(e)},status=status.HTTP_401_UNAUTHORIZED) 

        try:
            user_book_service_id = kwargs.get("user_book_service_id",None)

            user_book_obj = get_object_or_none(UserBookService,id=user_book_service_id)
            if user_book_obj:
                return Response({"status":"success","data":self.serializer_class(user_book_obj).data},status=status.HTTP_200_OK)
            else:
                return Response({"status":"error","message":"User book service not found."},status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"status":"error","message":"Error occured(%s)"%str(e)},status=status.HTTP_400_BAD_REQUEST)

