import grpc
# from google.protobuf.json_format import MessageToJson
from panabios_rpc.lab_test_proto import lab_test_pb2,lab_test_pb2_grpc
from django.http import HttpResponseRedirect
from booking_manager_api.models import BookableService
from rpc_client_app.calls import *
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view


@api_view(['GET'])
def populate_bookable_service(request):
    try:
        tests = all_tests()
        if tests:
            for labtest in tests:
                BookableService.objects.update_or_create(service_id=labtest,service_type=BookableService.TEST,
                                                    defaults={"service_id":labtest,"service_type":BookableService.TEST})
            return Response({"status":"success","message":"Services successfully uploaded"},status=status.HTTP_200_OK)        
        else:
            return Response({"status":"error","message":"Uploading services failed"},status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response({"status":"error","message":"Uploading services stopped"},status=status.HTTP_400_BAD_REQUEST)
