from intel_api.models import UserEntity,AccessToken
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from intel_api.serializers.accounts_serializers import IntelUserLabResponseSerializer
from intel_api.serializers.lab_serializers import IntelGetLabByLabNameSerializer,IntelGetLabByRegNumberSerializer
from booking_manager_api.models.util import get_object_or_none
from google.protobuf.json_format import MessageToJson
import json

from intel_api.views.authentication import GetRequestAuthenticationBase

from rpc_client_app.calls import get_lab_by_registration_number,get_lab_by_lab_name


class IntelGetLabByRegistrationNumberView(APIView):

    def get(self,request):
        try:
            data = dict()
            registration_number = request.GET.get("reg_number",None)
            data['registration_number'] = registration_number
            serializer = IntelGetLabByRegNumberSerializer(data=data)
            if serializer.is_valid():
                reg_num = serializer.validated_data['registration_number']
                lab = get_lab_by_registration_number(reg_number=reg_num)
                if lab:
                    return Response({"status":"success",
                        "data":IntelUserLabResponseSerializer(json.loads(MessageToJson(lab))).data},status=status.HTTP_200_OK)
                else:
                    return Response({"status":"error","message":"Lab not found"},status=status.HTTP_404_NOT_FOUND)

            return Response({"status":"error","message":serializer.errors},status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            return Response({"status":"error","message":str(e)},status=status.HTTP_404_NOT_FOUND)

    def post(self,request):
        return Response({"status":"error","message":"Request not allowed"},status=status.HTTP_400_BAD_REQUEST)


class IntelGetLabByLabNameView(APIView):#GetRequestAuthenticationBase

    def get(self,request):
        try:
            data = dict()
            # user = self.authenticate(request)
            lab_name = request.GET.get("lab_name",None)
            data['lab_name'] = lab_name
            serializer = IntelGetLabByLabNameSerializer(data=data)
            if serializer.is_valid():
                lab_name = serializer.validated_data['lab_name']
                lab = get_lab_by_lab_name(lab_name=lab_name)
                if lab:
                    return Response({"status":"success",
                        "data":IntelUserLabResponseSerializer(json.loads(MessageToJson(lab))).data},status=status.HTTP_200_OK)
                else:
                    return Response({"status":"error","message":"Lab not found"},status=status.HTTP_404_NOT_FOUND)

            return Response({"status":"error","message":serializer.errors},status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            return Response({"status":"error","message":str(e)},status=status.HTTP_404_NOT_FOUND)

    def post(self,request):
        return Response({"status":"error","message":"Request not allowed"},status=status.HTTP_400_BAD_REQUEST)

