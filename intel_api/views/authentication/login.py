from intel_api.models import UserEntity,AccessToken,ExternalEntity
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from intel_api.serializers.auth_login_serializer import IntelAuthLoginSerializer
from rpc_client_app.calls import fetch_user_profile,fetch_user_lab
from booking_manager_api.models.util import get_object_or_none

from intel_api.models.access_token import generate_key


class IntelAuthLogin(APIView):
    """
    Request format:
    POST
        {
            "session_key": "some session key",
            "username": "mike@mike.com"
        }
    Response:
        Patient
        {
          "status": "success",
          "data": {
            "user_name": "mike@mike.com",
            "token": "27d60ce08eae5644021804bd69eec094298605b7",
            "user_group": "Patient"
          }
        }

        Lab User
            {
              "status": "success",
              "data": {
                "lab_registration_number": "c4edbbea-44d9-451b-b277-1f3519b45b1f",
                "lab_id": 5,
                "user_name": "lavtech@lavtexh.com",
                "token": "1947031a3608dd4a1de89eadffd4497f4e6b9288",
                "user_group": "Lab Technician"
              }
            }
    """
    permission_classes = (permissions.AllowAny,)
    authentication_classes = ()
    
    data = dict()

    def post(self,request):
        serializer = IntelAuthLoginSerializer(data=request.data)
        try:        
            if serializer.is_valid():
                username = serializer.validated_data['username']
                session_key = serializer.validated_data['session_key']
                user = fetch_user_profile(username)
                if user:
                    if user.is_lab_user:
                        user_lab = fetch_user_lab(user.id)
                        if user_lab:
                            self.data["lab_registration_number"] = user_lab.registration_number
                            self.data["lab_id"] = user_lab.id
                            x_entity, _ = ExternalEntity.objects.get_or_create(entity_id=user_lab.id,entity_reg=user_lab.registration_number,
                                                                            entity_type=ExternalEntity.LAB)
                        else:
                            return Response({"status":"error","message":"User lab not found"},status=status.HTTP_404_NOT_FOUND)
                    
                    user_entity, created = UserEntity.objects.get_or_create(user_profile_id=user.id,username=username)
                    if created:
                        #new login
                        access_token = AccessToken.create(user_entity=user_entity,session_key=session_key)
                    else:
                        # access_token = get_object_or_none(AccessToken,user_entity=user_entity,session_key=session_key)
                        instances = AccessToken.objects.filter(user_entity=user_entity)
                        if instances.exists():
                            instances.update(is_login=False) #log all Access token instance out
                        #create new access token object with new session key
                        access_token = AccessToken.objects.create(user_entity=user_entity,session_key=session_key,token=generate_key())

                    if access_token:
                        # if not access_token.is_login:
                        #     return Response({"status":"error","message":"user logged out."},status=status.HTTP_404_NOT_FOUND)
                        self.data['user_name'] = access_token.user_entity.username
                        self.data['token'] = access_token.token
                        self.data['user_group'] = user.group
                        return Response({"status":"success","data":self.data},status=status.HTTP_200_OK)
                    else:
                        return Response({"status":"error","message":"user not found or logged out."},status=status.HTTP_401_UNAUTHORIZED)
                else:
                    return Response({"status":"error","message":"Requested user not found"},status=status.HTTP_401_UNAUTHORIZED)
            else:
                return Response({"status":"error","message":serializer.errors},status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            return Response({"status":"error","message":e.detail if hasattr(e, "detail") else [str(e)]},status=status.HTTP_400_BAD_REQUEST)

    def get(self,request):
        return Response({"status":"error","message":"Request not allowed"},status=status.HTTP_400_BAD_REQUEST)
