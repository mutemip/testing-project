from rest_framework import serializers


class IntelUserProfileRequestSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    # token = serializers.CharField(required=True)


class IntelUserProfileResponseSerializer(serializers.Serializer):
    id  = serializers.IntegerField(required=True)
    code  = serializers.CharField(required=False)
    gender  = serializers.CharField(required=False)
    date_of_birth  = serializers.CharField(required=False)
    group  = serializers.CharField(required=True)
    firstName  = serializers.CharField(required=True)
    lastName  = serializers.CharField(required=True)
    email  = serializers.CharField(required=False)
    phoneNumber  = serializers.CharField(required=False)
    nationality  = serializers.CharField(required=False)


class IntelUserLabResponseSerializer(serializers.Serializer):
    id  = serializers.IntegerField(required=True)
    name = serializers.CharField()
    country = serializers.CharField()
    region = serializers.CharField(required=False)
    streetAddress1 = serializers.CharField()
    streetAddress2 = serializers.CharField()
    zipcode = serializers.CharField(required=False)
    email = serializers.EmailField()
    registrationNumber = serializers.CharField()
    phoneNumber = serializers.CharField()
    proprietaryCode = serializers.CharField(required=False)
    ttCompliant = serializers.BooleanField(required=False)
    city = serializers.CharField(required=False)
    submitTestToNationalRepo = serializers.BooleanField()
    isApproved = serializers.BooleanField()
    logo = serializers.CharField(required=False)
    bio = serializers.CharField(required=False)
    website = serializers.CharField(required=False)
    linkedin = serializers.CharField(required=False)
    twitter = serializers.CharField(required=False)
    instagram = serializers.CharField(required=False)
