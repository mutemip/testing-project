from rest_framework import serializers

class IntelAuthLoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    session_key = serializers.CharField(required=True)
