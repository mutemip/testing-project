from rest_framework import generics, status
from rest_framework.response import Response
from intel_api.views.authentication import GetRequestAuthenticationBase
from rest_framework.views import APIView
from booking_manager_api.models import  EntityService, EntityBookingSchedule
from clients_booking_api.models import UserBookService


class DashboardMetricsView(GetRequestAuthenticationBase,APIView):
    """
    Format:
        import requests

        url = "http://localhost:8000/api/v1/booking/manager/dashboard/summary/"

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
          "data": 4
        }
    """

    def get(self,request):
        try:
            user = self.authenticate(request)
        except Exception as e:
            return Response({"status":"error","message":"%s"%str(e)},status=status.HTTP_401_UNAUTHORIZED) 

        try:
            metrics = dict()
            if user.is_lab_user():
                external_entity = user.get_external_entity()
                booked_services = UserBookService.get_external_entity_bookings(external_entity).count()
                entity_services = EntityService.get_entity_services(external_entity).count()
                entity_booking_schedules = EntityBookingSchedule.entity_booking_schedules(external_entity).count()

                metrics["entity_services"] = entity_services
                metrics["entity_booking_schedules"] = entity_booking_schedules
            else:
                booked_services = UserBookService.get_patient_bookings(user.user_entity).count()
            metrics['total_bookings'] = booked_services
            return Response({"status":"success","data":metrics},status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"status":"error","message":"Error occured(%s)"%str(e)},status=status.HTTP_400_BAD_REQUEST)
            