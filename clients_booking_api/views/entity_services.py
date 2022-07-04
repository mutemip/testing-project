from rest_framework import generics, status
from rest_framework.response import Response
from booking_manager_api.models import EntityService,BookableService
from intel_api.views.authentication import GetRequestAuthenticationBase

# from django.db.models import Q

class ClientEntityServiceListView(GetRequestAuthenticationBase,generics.ListAPIView):
    
    def get_objects(self,qs,external_entity_country,external_entity_name,type_,service_name,country=True):
        arr = list()
        for obj in qs.filter(service__service_type=type_):
            service = obj.service.detail()
            external_entity = obj.bookable_entity.detail
            if country:
                if (service.name == service_name) and (external_entity.name == external_entity_name) and \
                    (external_entity.country == external_entity_country):
                    arr.append(obj)
            else:
                if service.name == service_name and external_entity.name == external_entity_name:
                    arr.append(obj)
        return arr

    def serialize_services(self,objs):
        services = list()
        for obj in objs:
            service = obj.service.detail()
            entity = obj.bookable_entity.detail

            services.append({
                "bookable_entity": entity.registration_number if entity.registration_number else "", 
                "bookable_entity_name": entity.name if entity.name else "", 
                "bookable_entity_country": entity.country if entity.country else "", 
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
            # user = self.authenticate(request)

            data = request.GET
            type_ = data.get('type',None)
            external_entity_country = data.get('external_entity_country',None)
            external_entity_name = data.get('external_entity_name',None)
            service_name = data.get('service_name',None)

            qs = EntityService.objects.all().select_related('bookable_entity','service')
            if type_ and external_entity_country and external_entity_name and service_name:
                if type_ == "all":
                    return Response({"status": "success", "data": self.serialize_services(qs)},status=status.HTTP_200_OK)
                elif external_entity_country == "all":
                    return Response({"status": "success", "data": self.serialize_services(
                        self.get_objects(
                            qs,
                            external_entity_country=external_entity_country,
                            external_entity_name=external_entity_name,
                            service_name=service_name,
                            type_=type_,
                            country=False))},status=status.HTTP_200_OK)
                else:
                    return Response({"status": "success", "data": self.serialize_services(
                        self.get_objects(
                            qs,
                            external_entity_country=external_entity_country,
                            external_entity_name=external_entity_name,
                            service_name=service_name,
                            type_=type_))},status=status.HTTP_200_OK)
            else:
                return Response({"status": "success", "data": self.serialize_services(qs)},status=status.HTTP_200_OK)
            
        except Exception as e:
            return Response({"status":"error","message":"Error occured(%s)."%str(e)},status=status.HTTP_400_BAD_REQUEST)
