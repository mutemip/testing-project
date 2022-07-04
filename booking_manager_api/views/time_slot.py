from intel_api.models import UserEntity,AccessToken
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import json
from booking_manager_api.models import TimeSlot
from intel_api.views.authentication import GetRequestAuthenticationBase
from booking_manager_api.serializers import TimeSlotSerializer

TIME_FORMAT = "%H:%M:%S"

class TimeSlotAView(GetRequestAuthenticationBase,APIView):
    """
    Request Format:
    GET
        interval = 60

    hearder:
        Authorization: Token 1947031a3608dd4a1de89eadffd4497f4e6b9288
        session-key = your session key

    Response:
        {
          "status": "success",
          "data": [
            {
              "id": 1,
              "start": "00:00:00",
              "end": "01:00:00",
              "interval": 60
            },...
          ]
        }
    Example:
        import requests
        url = "http://localhost:8000/api/v1/manager/time/slots/interval/"
        payload = "interval=60"
        headers = {
            "session-key": "BDUhANPuZs",
            "Content-Type": "application/x-www-form-urlencoded",
            "Authorization": "Token ac9c93b147a701dea08ee41f9a224a27b0c06ffe"
        }
        response = requests.request("GET", url, data=payload, headers=headers)
        print(response.text)
    """
    def serialize_slots(self,slots):
        data = list()
        for slot in slots:
            data.append({"id":slot.id,"start":slot.start_time.strftime(TIME_FORMAT),"end":slot.end_time.strftime(TIME_FORMAT),"interval":slot.interval_in_minute})
        return data


    def get(self,request,**kwargs):
        try:
            user = self.authenticate(request)
        except Exception as e:
            return Response({"status":"error","message":"%s"%str(e)},status=status.HTTP_401_UNAUTHORIZED) 

        interval = kwargs.get('interval',None)
        if interval:
            try: 
                if user.is_lab_user():
                    time_slots = TimeSlot.get_slots_by_interval(interval)
                    return Response({"status":"success","data":self.serialize_slots(time_slots)},status=status.HTTP_200_OK)
                else:
                    return Response({"status":"error","message":"Unauthorized user access."},status=status.HTTP_401_UNAUTHORIZED)
            except Exception as e:
                return Response({"status":"error","message":"Error occured(%s)"%str(e)},status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"status":"error","message":"please provide an interval."},status=status.HTTP_400_BAD_REQUEST)
        
    def post(self,request):
        try:
            user = self.authenticate(request)
        except Exception as e:
            return Response({"status":"error","message":"%s"%str(e)},status=status.HTTP_401_UNAUTHORIZED) 
        return Response({"status":"error","message":"Request not allowed"},status=status.HTTP_400_BAD_REQUEST)
