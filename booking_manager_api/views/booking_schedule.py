from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from booking_manager_api.serializers import BookingScheduleSerializer
from intel_api.serializers.accounts_serializers import IntelUserProfileRequestSerializer
from intel_api.models import UserEntity,ExternalEntity
from booking_manager_api.models.util import get_object_or_none
from booking_manager_api.models import EntityService
from intel_api.views.authentication import GetRequestAuthenticationBase

from booking_manager_api.models import EntityWorkingDays,EntityBookingSchedule,DaysOfTheWeek,TimeSlot
from rest_framework.views import APIView

class BookingScheduleView(GetRequestAuthenticationBase,APIView):
    """
        Request: Post
            {
                "schedule":
                    [
                        {
                            "day_of_the_week":1,
                            "time_slots":
                                [
                                    {
                                        "slot_id":1,
                                        "max_bookee":100
                                    },
                                    {
                                        "slot_id":2,
                                        "max_bookee":120
                                    },
                                    {
                                        "slot_id":3,
                                        "max_bookee":105
                                    },...
                                ]
                        },            
                        {
                            "day_of_the_week":2,
                            "time_slots":
                                [
                                    {
                                        "slot_id":4,
                                        "max_bookee":100
                                    },
                                    {
                                        "slot_id":5,
                                        "max_bookee":120
                                    },...
                                ]
                        },...
                    ]
            }

        Headers:
            Authorization: Token 1947031a3608dd4a1de89eadffd4497f4e6b9288
            session-key = your session key

        Response:
            {
              "status": "success",
              "message": "Booking schedule successfully created."
            }
    """

    serializer_class = BookingScheduleSerializer

    def post(self, request, *args, **kwargs):
        try:
            user = self.authenticate(request)
        except Exception as e:
            return Response({"status":"error","message":"%s"%str(e)},status=status.HTTP_401_UNAUTHORIZED) 

        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            try: 
                external_entity = user.get_external_entity()
                if external_entity:
                    schedules = serializer.validated_data['schedule']
                    for schedule in schedules:
                        day = get_object_or_none(DaysOfTheWeek,id=schedule['day_of_the_week'])
                        if day:
                            time_slots = schedule['time_slots']
                            entity_working_day,_ = EntityWorkingDays.objects.get_or_create(bookable_entity=external_entity,day=day,created_by=user.user_entity)
                            for slot in time_slots:
                                t_slot = get_object_or_none(TimeSlot,id=slot['slot_id'])
                                if t_slot:
                                    if entity_working_day:
                                        is_created = EntityBookingSchedule.objects.filter(
                                            entity_working_days__bookable_entity=external_entity,
                                            entity_working_days=entity_working_day,
                                            timeslot=t_slot
                                        )
                                        if not is_created.exists():
                                                EntityBookingSchedule.create(
                                                    entity_working_days=entity_working_day,timeslot=t_slot,
                                                    created_by=user.user_entity,maximum_bookee=slot['max_bookee'])
                                        else:
                                            return Response({
                                                "status":"error",
                                                "message":"Schedule already exists."},status=status.HTTP_400_BAD_REQUEST)
                                    else:
                                        return Response({
                                            "status":"error",
                                            "message":"Error creating entity working days."},status=status.HTTP_400_BAD_REQUEST)
                                else:
                                    return Response({"status":"error","message":"Error getting the apropriate time slot."},status=status.HTTP_404_NOT_FOUND)
                        else:
                            return Response({"status":"error","message":"Error getting the apropriate day of the week."},status=status.HTTP_404_NOT_FOUND)
                    
                    return Response({"status": "success", "message": "Booking schedule successfully created."},status=status.HTTP_200_OK)
                else:
                    return Response({"status":"error","message":"User does not belong to a lab entity."},status=status.HTTP_400_BAD_REQUEST)
            except Exception as e:
                return Response({"status":"error","message":"Error occured(%s)."%str(e)},status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"status":"error","message":serializer.errors},status=status.HTTP_400_BAD_REQUEST)




class EntityBookingSchedules(GetRequestAuthenticationBase,APIView):
    """
        Request Format:
            import requests

            url = "http://localhost:8000/api/v1/booking/manager/entity/booking/schedules/"

            headers = {
                "session-key": "BDUhANPuZs",
                "Content-Type": "application/json",
                "Authorization": "Token ac9c93b147a701dea08ee41f9a224a27b0c06ffe"
            }

            response = requests.request("GET", url, headers=headers)

            print(response.text)

        Response:
            {
              "status": "success",
              "data": {
                "schedule": [
                  {
                    "day_of_the_week": 1,
                    "time_slots": [
                      {
                        "slot_id": 1,
                        "max_bookee": 100
                      },
                      {
                        "slot_id": 2,
                        "max_bookee": 120
                      },
                      {
                        "slot_id": 3,
                        "max_bookee": 105
                      }
                    ]
                  },
                  {
                    "day_of_the_week": 2,
                    "time_slots": [
                      {
                        "slot_id": 4,
                        "max_bookee": 120
                      },
                      {
                        "slot_id": 5,
                        "max_bookee": 105
                      }
                    ]
                  }
                ]
              }
            }
    """

    def serialize_data(self,bookings):
        try:        
            schedule = list()
            for booking in bookings:
                s = dict()
                s['day_of_the_week'] = booking.day.day
                b_schedules = EntityBookingSchedule.objects.filter(entity_working_days=booking)
                slots = list()
                for item in b_schedules:
                    slots.append({"slot":{
                        "start_time":item.timeslot.start_time,"end_time":item.timeslot.end_time,
                        "interval":item.timeslot.interval_in_minute},"max_bookee":item.maximum_bookee})
                s['time_slots'] = slots
                schedule.append(s)
            return {'schedule':schedule}
        except Exception as e:
            raise Exception("Error serializing data.")


    def get(self,request):
        try:
            user = self.authenticate(request)
        except Exception as e:
            return Response({"status":"error","message":"%s"%str(e)},status=status.HTTP_401_UNAUTHORIZED) 

        try:
            user_external_entity = user.get_external_entity()
            if user_external_entity:
                entity_bookings = EntityWorkingDays.get_entity_bookings(user_external_entity)
                if entity_bookings.exists():
                    return Response({"status": "success", "data":self.serialize_data(entity_bookings)},status=status.HTTP_200_OK)
                else:
                    return Response({"status":"error","message":"No bookings available."},status=status.HTTP_404_NOT_FOUND)
            else:
                return Response({"status":"error","message":"External entity not found."},status=status.HTTP_404_NOT_FOUND)

        except  Exception as e:
            return Response({"status":"error","message":"Error occured(%s)."%str(e)},status=status.HTTP_400_BAD_REQUEST)
