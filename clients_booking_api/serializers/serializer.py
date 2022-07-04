from rest_framework import serializers
from clients_booking_api.models.bookservice import UserBookService
from booking_manager_api.models.util import get_object_or_none
from booking_manager_api.models import EntityService, EntityBookingSchedule

from booking_manager_api.serializers import EntityServiceSerializer
from clients_booking_api.models import UserBookTravelInformation
from google.protobuf.json_format import MessageToJson
import json
from datetime import date


class UserBookTravelInformationSerializer(serializers.ModelSerializer):
    travel_date = serializers.DateTimeField(format="%d-%m-%Y", input_formats=['%d-%m-%Y', 'iso-8601'])
    class Meta:
        model = UserBookTravelInformation
        fields = ("travel_date","departure_country","arrival_country","passport_number", "transport_operator" )

    def create(self,validated_data):
        return UserBookTravelInformation.create(
                userbookservice=validated_data['user_booking'],
                travel_date=validated_data["travel_date"],
                departure_country=validated_data['departure_country'],
                arrival_country=validated_data['arrival_country'],
                passport_number=validated_data['passport_number'],
                transport_operator=validated_data['transport_operator']
            )


class UserBookServiceSerializer(serializers.Serializer):
    booked_by = serializers.SerializerMethodField(required=False,read_only=True)
    booked_entity_service = serializers.IntegerField()
    schedule_date = serializers.DateField(format="%d-%m-%Y", input_formats=['%d-%m-%Y', 'iso-8601'])
    entity_booking_schedule = serializers.IntegerField()
    # code = serializers.CharField(required=False,read_only=True)
    # payed = serializers.BooleanField(required=False)
    travel_info = UserBookTravelInformationSerializer(required=False)


    def create(self, validated_data):
        today = date.today()
        service_id = validated_data["booked_entity_service"]
        booking_date = validated_data["schedule_date"]
        entity_booking_schedule_id = validated_data["entity_booking_schedule"]
        user = validated_data["user"]
        travel_info = validated_data.get('travel_info',None)
        if booking_date < today:
            raise serializers.ValidationError("booking date cannot be in the past.")

        if user:
            entity_service = get_object_or_none(EntityService,id=service_id)
            if entity_service:
                entity_booking_schedule = get_object_or_none(EntityBookingSchedule,id=entity_booking_schedule_id)
                if entity_booking_schedule:
                    try:
                        user_booking = UserBookService.create(booked_by=user.user_entity,date=booking_date,entity_service=entity_service,
                            booking_schedule=entity_booking_schedule)
                        if not user_booking:
                            raise Exception("Service booking record exists.")
                        if travel_info:
                            xtra_info = UserBookTravelInformationSerializer(data=travel_info)
                            if xtra_info.is_valid():
                                xtra_info.save(user_booking=user_booking)

                        return user_booking
                    except Exception as e:
                        raise serializers.ValidationError("{}".format(str(e)))
                else:
                    raise serializers.ValidationError("Entity schedule not found")
            else:
                raise serializers.ValidationError("Entity service not found")
        else:
            raise serializers.ValidationError("User must be supplied.")

    def get_booked_by(self,instance):
        return instance.booked_by.username

    # def get_code(self,instance):
    #     return instance.code

    # def get_booked_entity_service(self,instance):
    #     return instance.booked_entity_service.id

    # def get_entity_booking_schedule(self,instance):
    #     return instance.entity_booking_schedule.id


class ManagerUserBookServiceSerializer(serializers.ModelSerializer):    
    booked_by = serializers.SerializerMethodField(required=False,read_only=True)
    booked_entity_service = serializers.SerializerMethodField(read_only=True)
    entity_booking_schedule = serializers.SerializerMethodField(read_only=True)
    travel_info = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = UserBookService
        fields = ('id','created_at','booked_by','booked_entity_service','schedule_date','entity_booking_schedule','code','payed','travel_info')

    def get_booked_by(self,instance):
        return json.loads(MessageToJson(instance.booked_by.user_profile()))
        # return instance.booked_by.username


    def get_entity_booking_schedule(self,instance):
        data = instance.entity_booking_schedule
        return {
            'working day': data.entity_working_days.day.day,
            "time_slot": "{} - {}".format(data.timeslot.start_time,data.timeslot.end_time),
            "max_bookee": data.maximum_bookee,
        }
        
    def get_booked_entity_service(self,instance):
        data = instance.booked_entity_service
        return{
            "external_entity":data.bookable_entity.detail.name,
            "service_name": data.service_name,
            "service": data.service.detail().name,
            "price": {"amount":str(data.price.amount),"currency":str(data.price.currency)}
        }

    def get_travel_info(self,instance):
        return UserBookTravelInformationSerializer(UserBookTravelInformation.objects.get(userbookservice=instance)).data
