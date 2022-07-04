from booking_manager_api.models import EntityService,BookableService
from intel_api.models import ExternalEntity
from rest_framework import serializers
from booking_manager_api.models.util import get_object_or_none
from djmoney.money import Money

class EntityServiceSerializer(serializers.ModelSerializer):
    bookable_entity = serializers.CharField()
    service = serializers.IntegerField()
    currency = serializers.CharField()
    username = serializers.CharField()
    service_name = serializers.CharField()

    class Meta:
        model = EntityService
        fields = '__all__'

    def create(self, validated_data):
        reg_no = validated_data["bookable_entity"]
        service_id = validated_data["service"]
        price = validated_data["price"]
        payment_required = validated_data["payment_required"]
        sharing_consent_required = validated_data["sharing_consent_required"]
        currency = validated_data["currency"]
        service_name = validated_data["service_name"]

        external_entity = get_object_or_none(ExternalEntity, entity_reg=reg_no)
        service = get_object_or_none(BookableService, service_id=service_id)
        if not external_entity:
            raise serializers.ValidationError("Entity not found or invalid registration number submitted.")
        if not service:
            raise serializers.ValidationError("Service not found or invalid service id provided.")
        if not EntityService.objects.filter(bookable_entity=external_entity,service=service).exists():
            try:
                entity_service = EntityService.create(service_name=service_name,bookable_entity=external_entity,service=service,price=Money(price, currency),
                                        payment_required=payment_required,sharing_consent_required=sharing_consent_required)
                return entity_service
            except Exception as e:
                raise serializers.ValidationError('{}'.format(str(e)))
        else:
            raise serializers.ValidationError("Entity service already exists.")