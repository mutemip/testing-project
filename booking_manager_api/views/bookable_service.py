from rest_framework import generics, status
from rest_framework.response import Response

from booking_manager_api.serializers import BookableServicesSerializer
from booking_manager_api.models import BookableService

from intel_api.views.authentication import GetRequestAuthenticationBase
from rest_framework.views import APIView
from booking_manager_api.models.util import get_object_or_none


class BookableServiceView(GetRequestAuthenticationBase,generics.ListAPIView):
    """
    Request format:
    GET
    
    Format:
        localhost:8000/api/v1/booking/manager/list/bookable/services/Test/
        pass Test as url args
        
    header:
        Authorization: Token 1947031a3608dd4a1de89eadffd4497f4e6b9288
        session-key = your session key

    Response:
        {
          "status": "success",
          "data": [
            {
              "service_id": 1,
              "service_type": "Test",
              "details": {
                "name": "test",
                "lonic_code": "test",
                "type": "Diagnostic",
                "disease": "",
                "method": "",
                "target": ""
              }
            },...
          ]
        }
    """
    serializer_class = BookableServicesSerializer

    def list(self, request,**kwargs):
        try:
            user = self.authenticate(request)
        except Exception as e:
            return Response({"status":"error","message":"%s"%str(e)},status=status.HTTP_401_UNAUTHORIZED) 

        data = kwargs.get('type',None)
        if data:
            try:
                
                # if user.user_entity.user_profile().is_lab_user:
                bookable_service = BookableService.objects.filter(service_type=data)
                # if bookable_service.exists():
                serializer = BookableServicesSerializer(bookable_service, many=True)
                return Response({"status": "success", "data": serializer.data},status=status.HTTP_200_OK)
                # else:
                #     return Response({"status": "error", "message": "Requesting user must be a lab user."},status=status.HTTP_400_BAD_REQUEST)
                
            except Exception as e:
                return Response({"status":"error","message":"An error occured(%s)."%str(e)},status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"status":"error","message":"Please provide a type as url arguement."},status=status.HTTP_400_BAD_REQUEST)


class BookableServiceDetailView(GetRequestAuthenticationBase,APIView):

    def serialize_data(self,data):
        obj = data.detail()
        if obj:
            return {
                "service_id":obj.id,
                "name":obj.name,
                "lonic_code":obj.lonic_code,
                "type":obj.type,
                "disease":obj.disease,
                "target":obj.target if obj.target else "",
                "method":obj.method if obj.method else "",

            }

    def get(self, request,**kwargs):
        service_id = kwargs.get('service_id',None)
        if service_id:
            try:
                user = self.authenticate(request)
                if user.user_entity.user_profile().is_lab_user:
                    
                    bookable_service = get_object_or_none(BookableService,service_id=service_id)
                    # if bookable_service:
                    return Response({"status": "success", "data": self.serialize_data(bookable_service)})
                    
                else:
                    return Response({"status": "error", "message": "Requesting user must be a lab user."},status=status.HTTP_400_BAD_REQUEST)
            except Exception as e:
                return Response({"status":"error","message":"Error occured(%s)."%str(e)},status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"status":"error","message":"Please provide a service id as url arguement."},status=status.HTTP_400_BAD_REQUEST)
