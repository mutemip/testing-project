from intel_api.models import UserEntity,AccessToken
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from intel_api.serializers.accounts_serializers import IntelUserProfileRequestSerializer,IntelUserProfileResponseSerializer,\
                                                         IntelUserLabResponseSerializer
from booking_manager_api.models.util import get_object_or_none
from google.protobuf.json_format import MessageToJson
import json

from intel_api.views.authentication import GetRequestAuthenticationBase

class IntelUserProfileView(GetRequestAuthenticationBase,APIView):
    """
    Request Format:

    hearder:
        Authorization: Token 1947031a3608dd4a1de89eadffd4497f4e6b9288
        
        session-key = your session key

    Response:
        {
          "status": "success",
          "data": {
            "id": 3,
            "code": "PA6947432",
            "gender": "M",
            "group": "Patient"
          }
        }

    example:
        import requests
        url = "http://localhost:8000/api/v1/intel/userprofile/"
        headers = {
            "session-key": "BDUhANPuZs",
            "Authorization": "Token ac9c93b147a701dea08ee41f9a224a27b0c06ffe"
        }
        response = requests.request("GET", url, headers=headers)
        print(response.text)
    """
    serializer_class = IntelUserProfileResponseSerializer

    def get(self,request):
        try:
            user = self.authenticate(request)
        except Exception as e:
            return Response({"status":"error","message":"%s"%str(e)},status=status.HTTP_401_UNAUTHORIZED) 

        # try:
        userprofile = MessageToJson(user.user_entity.user_profile())
        if not userprofile:
            return Response({"status":"error","message":"UserProfile is None,most likely rpc error."},status=status.HTTP_400_BAD_REQUEST)
        serializer = self.serializer_class(data=json.loads(userprofile))
        if serializer.is_valid():
            return Response({"status":"success","data":self.serializer_class(json.loads(userprofile)).data},status=status.HTTP_200_OK)
        else:
            return Response({"status":"error","message":serializer.errors},status=status.HTTP_400_BAD_REQUEST)

        # except Exception as e:
        #     return Response({"status":"error","message":"User Authentication failed"},status=status.HTTP_404_NOT_FOUND)

    def post(self,request):
        try:
            user = self.authenticate(request)
        except Exception as e:
            return Response({"status":"error","message":"%s"%str(e)},status=status.HTTP_401_UNAUTHORIZED)
        return Response({"status":"error","message":"Request not allowed"},status=status.HTTP_400_BAD_REQUEST)


class IntelUserLabView(GetRequestAuthenticationBase,APIView):
    """
    Request Format:
    GET

    hearder:
        Authorization: Token 1947031a3608dd4a1de89eadffd4497f4e6b9288
        session-key = your session key
    Response:
        {
          "status": "success",
          "data": {
            "id": 5,
            "name": "lab3_updated",
            "country": "Nigeria",
            "region": "Abuja",
            "streetAddress1": "Abuja",
            "streetAddress2": "Abuja",
            "zipcode": "1234",
            "email": "lab3@lab3.com",
            "registrationNumber": "c4edbbea-44d9-451b-b277-1f3519b45b1f",
            "phoneNumber": "(+234)111111111123",
            "proprietaryCode": "233132"
          }
        }
    """
    def get(self,request):
        try:
            user = self.authenticate(request)
        except Exception as e:
            return Response({"status":"error","message":"%s"%str(e)},status=status.HTTP_401_UNAUTHORIZED) 

        try:
            user_lab = MessageToJson(user.user_entity.get_lab())
            return Response({"status":"success","data":IntelUserLabResponseSerializer(json.loads(user_lab)).data},status=status.HTTP_200_OK)        
        except Exception as e:
            return Response({"status":"error","message":"Error occured,please try again later."},status=status.HTTP_400_BAD_REQUEST)

    def post(self,request):
        try:
            user = self.authenticate(request)
        except Exception as e:
            return Response({"status":"error","message":"%s"%str(e)},status=status.HTTP_401_UNAUTHORIZED) 
        return Response({"status":"error","message":"Request not allowed"},status=status.HTTP_400_BAD_REQUEST)


