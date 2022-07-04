from booking_manager_api.models import TimeSlot
from rest_framework import serializers



class TimeSlotSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    interval = serializers.IntegerField(required=True)
