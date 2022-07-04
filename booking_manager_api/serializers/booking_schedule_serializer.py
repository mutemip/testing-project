from rest_framework import serializers

class SlotsSerializer(serializers.Serializer):
    slot_id = serializers.IntegerField(required=True)
    max_bookee = serializers.IntegerField(required=True)


class DaysOfTheWeekSerializer(serializers.Serializer):
    time_slots = SlotsSerializer(required=True,many=True)
    day_of_the_week = serializers.IntegerField()

class BookingScheduleSerializer(serializers.Serializer):
    schedule = DaysOfTheWeekSerializer(many=True) 