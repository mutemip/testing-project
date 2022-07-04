from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from booking_manager_api.serializers import EntityServiceSerializer
from intel_api.serializers.accounts_serializers import IntelUserProfileRequestSerializer
from intel_api.models import UserEntity,AccessToken,ExternalEntity
from booking_manager_api.models.util import get_object_or_none
from booking_manager_api.models import EntityService
from intel_api.views.authentication import GetRequestAuthenticationBase

class EntityServiceView(GetRequestAuthenticationBase,generics.CreateAPIView):
    """
    Request format:

    POST
        {
            "bookable_entity":"c4edbbea-44d9-451b-b277-1f3519b45b1f",
            "service": 8,
            "price": 542,
            "payment_required": "True",
            "sharing_consent_required":"False",
            "currency": "USD"
            "username": "lavtech@lavtexh.com"
        }

    hearder:
        Authorization: Token 1947031a3608dd4a1de89eadffd4497f4e6b9288
        session-key: "some key"

    Response:
        {
          "status": "success",
          "message": "service created."
        }
    """
    serializer_class = EntityServiceSerializer

    def post(self, request, *args, **kwargs):
        try:
            user = self.authenticate(request)
        except Exception as e:
            return Response({"status":"error","message":"%s"%str(e)},status=status.HTTP_401_UNAUTHORIZED) 

        data = request.data
        serializer = self.serializer_class(data=data)
        if serializer.is_valid():
            try:            
                # username = serializer.validated_data['username']
                if user.is_lab_user():
                    entity_service = serializer.save()
                    return Response({"status": "success","message": "service created."},status=status.HTTP_201_CREATED)
                else:
                    return Response({"status":"error","message":"Unathorized user access."},status=status.HTTP_401_UNAUTHORIZED)
            except Exception as e:
                return Response({"status":"error","message":e.detail if hasattr(e, "detail") else str(e)},status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"status": "error","message":serializer.errors}, status=status.HTTP_400_BAD_REQUEST)



class EntityServiceListView(GetRequestAuthenticationBase,generics.ListAPIView):
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
              "bookable_entity": "d2ad4a04-2aac-476f-83ad-003c2bd82c1e",
              "service_id": 12,
              "test": {
                "id": 1,
                "name": "Viral Test",
                "loinc_code": "00433",
                "disease": 0,
                "type": "Diagnostic",
                "method": "",
                "target": ""
              },
              "currency": "USD",
              "price": "53.00",
              "payment_required": true,
              "sharing_consent_required": true
            },
            {
              "bookable_entity": "d2ad4a04-2aac-476f-83ad-003c2bd82c1e",
              "service_id": 13,
              "test": {
                "id": 2,
                "name": "COVID-19",
                "loinc_code": "94566-4",
                "disease": 0,
                "type": "Diagnostic",
                "method": "",
                "target": ""
              },
              "currency": "USD",
              "price": "153.00",
              "payment_required": true,
              "sharing_consent_required": true
            }
          ]
        }

    """
    serializer_class = EntityServiceSerializer
    
    def get_objects(self,user):
        user_lab = user.user_entity.get_lab()
        if user_lab:
            external_entity = get_object_or_none(ExternalEntity,entity_id=user_lab.id,entity_reg=user_lab.registration_number,
                                                entity_type=ExternalEntity.LAB)
            if external_entity:
                return EntityService.objects.filter(bookable_entity=external_entity)

    def serialize_services(self,objs):
        services = list()
        for obj in objs:
            service = obj.service.detail()
            services.append({
                "bookable_entity": obj.bookable_entity.entity_reg if obj.bookable_entity else "", 
                "service_id": obj.id,
                "service_name":obj.service_name,
                "test": {
                    "id":service.id,"name":service.name,"loinc_code":service.lonic_code,"disease":service.disease,
                    "type":service.type,"method":service.method,"target":service.target
                }, 
                "currency": str(obj.price.currency) if obj.price else "", 
                "price": str(obj.price.amount) if obj.price else "", 
                "payment_required": obj.payment_required if obj.payment_required else False, 
                "sharing_consent_required": obj.sharing_consent_required if obj.sharing_consent_required else False, 
            })
        return services

    def list(self, request):
        try:
            user = self.authenticate(request)
        except Exception as e:
            return Response({"status":"error","message":"%s"%str(e)},status=status.HTTP_401_UNAUTHORIZED) 

        try:
            if user.is_lab_user():
                objs = self.get_objects(user) 
                if objs.exists():
                    return Response({"status": "success", "data": self.serialize_services(objs)},status=status.HTTP_200_OK)
                else:
                    return Response({"status":"error","message":"No services available"},status=status.HTTP_404_NOT_FOUND)
            else:
                return Response({"status":"error","message":"Unathorized user access."},status=status.HTTP_401_UNAUTHORIZED)
        except Exception as e:
            return Response({"status":"error","message":"Error occured(%s)."%str(e)},status=status.HTTP_400_BAD_REQUEST)
