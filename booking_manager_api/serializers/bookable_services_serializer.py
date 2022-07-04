from rest_framework import serializers
from booking_manager_api.models import BookableService


class BookableServicesSerializer(serializers.ModelSerializer):
    details = serializers.SerializerMethodField(read_only=True, allow_null=True)
    
    class Meta:
        model = BookableService
        fields = ['service_id','service_type','details']

    def get_details(self,instance):
        obj = instance.detail()
        if obj:
            return {
                "name": obj.name if obj.name else "", 
                "lonic_code": obj.lonic_code if obj.lonic_code else "", 
                "type": obj.type if obj.type else "", 
                "disease": obj.disease if obj.disease else "", 
                "method": obj.method if obj.method else "", 
                "target": obj.target if obj.target else "", 
            }