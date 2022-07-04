from intel_api.models import UserEntity,AccessToken,ExternalEntity
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from intel_api.serializers.auth_login_serializer import IntelAuthLoginSerializer
from rpc_client_app.calls import fetch_user_profile,fetch_user_lab
from booking_manager_api.models.util import get_object_or_none

class IntelAuthLogout(APIView):
    """
    Request format:
    POST
        {
            "session_key": "some session key",
            "username": "user name"
        }
    Response:
        {
          "status": "success",
          "message": "User successfully logged out."
        }
    """

    def post(self,request):
        serializer = IntelAuthLoginSerializer(data=request.data)
        try:        
            if serializer.is_valid(raise_exception=True):
                username = serializer.validated_data['username']
                session_key = serializer.validated_data['session_key']
                user = fetch_user_profile(username)
                if user:
                    user_entity = get_object_or_none(UserEntity,user_profile_id=user.id,username=username)
                    if user_entity:
                        access_token = get_object_or_none(AccessToken,user_entity=user_entity,session_key=session_key)
                        if access_token:
                            if access_token.is_login:
                                access_token.is_login = False
                                access_token.save()
                                return Response({"status":"success","message":"User successfully logged out."},status=status.HTTP_200_OK)
                            else:
                                return Response({"status":"error","message":"User already logged out, login."},status=status.HTTP_401_UNAUTHORIZED)
                        else:
                            return Response({"status":"error","message":"User not found"},status=status.HTTP_401_UNAUTHORIZED)
                    else:
                        return Response({"status":"error","message":"Entity not found"},status=status.HTTP_401_UNAUTHORIZED)
                else:
                    return Response({"status":"error","message":"Requested user not found"},status=status.HTTP_401_UNAUTHORIZED)
        except Exception as e:
            return Response({"status":"error","message":e.detail if hasattr(e, "detail") else [str(e)]},status=status.HTTP_400_BAD_REQUEST)

    def get(self,request):
        return Response({"status":"error","message":"Request not allowed"},status=status.HTTP_400_BAD_REQUEST)
