from intel_api.models import UserEntity,AccessToken
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import json
from booking_manager_api.models import DaysOfTheWeek
from intel_api.views.authentication import GetRequestAuthenticationBase
from intel_api.serializers.accounts_serializers import IntelUserProfileRequestSerializer


class DaysOfTheWeekView(GetRequestAuthenticationBase,APIView):
    """
    Request Format:
    GET

    hearder:
        Authorization: Token 1947031a3608dd4a1de89eadffd4497f4e6b9288
        session-key = your session key

    Response:
        {
          "status": "success",
          "data": [
            {
              "id": 1,
              "day": "Monday"
            },...
          ]
        }
    """
    def get(self,request):
        try:
            user = self.authenticate(request)
        except Exception as e:
            return Response({"status":"error","message":"%s"%str(e)},status=status.HTTP_401_UNAUTHORIZED) 

        try:
            if user.user_entity.user_profile().is_lab_user:
                days = DaysOfTheWeek.days_as_list()
                data=list()
                for day in days:
                    data.append({"id":day[0],"day":day[1]})
                return Response({"status":"success","data":data},status=status.HTTP_200_OK)
            else:
                return Response({"status":"error","message":"Unauthorized user access."},status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            return Response({"status":"error","message":"An error occured(%s)"%str(e)},status=status.HTTP_400_BAD_REQUEST)

    def post(self,request):
        try:
            user = self.authenticate(request)
        except Exception as e:
            return Response({"status":"error","message":"%s"%str(e)},status=status.HTTP_401_UNAUTHORIZED) 
        return Response({"status":"error","message":"Request not allowed"},status=status.HTTP_400_BAD_REQUEST)
