from rest_framework import serializers


class IntelGetLabByRegNumberSerializer(serializers.Serializer):
    registration_number = serializers.CharField(required=True)

class IntelGetLabByLabNameSerializer(serializers.Serializer):
    lab_name = serializers.CharField(required=True)