from clients_booking_api.models import UserBookService

from django_grpc_framework import proto_serializers
from intel_rpc.userbookservice import user_book_service_pb2
from rest_framework import serializers


class UserBookServiceProtoSerializer(proto_serializers.ModelProtoSerializer):
    booked_by = serializers.SerializerMethodField(read_only=True)
    booked_entity_service = serializers.SerializerMethodField(read_only=True)
    entity_booking_schedule = serializers.SerializerMethodField(read_only=True)
    
    class Meta:
        model = UserBookService
        proto_class = user_book_service_pb2.UserBookService
        fields = ["id","booked_by","booked_entity_service","schedule_date","entity_booking_schedule","code","payed"]


    def get_booked_by(self,instance):
        # user = instance.booked_by.user_profile()
        return instance.booked_by.username

    def get_entity_booking_schedule(self,instance):
        booking_schedule = instance.entity_booking_schedule  
        return str({
            	"day": booking_schedule.entity_working_days.day.day,
            	"maximum_bookee": booking_schedule.maximum_bookee,
            	"time_slot": "{} - {}".format(booking_schedule.timeslot.start_time,booking_schedule.timeslot.end_time)
        	})
    
    def get_booked_entity_service(self,instance):
        service = instance.booked_entity_service
        return str({
            	"name": service.service.detail().name,
            	"price": str(service.price)
        	})
   

