from rest_framework import serializers
from .models import buildings
from .models import Owner
from .models import addroom
from .models import customeraccount
class buildingSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    address = serializers.CharField(max_length=100)
    def create(self, validated_data):
        return buildings.objects.create(**validated_data)
 #########OWNER SERIALIZER

class ownerSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    def create(self, validated_data):
        return Owner.objects.create(**validated_data)

########Add room

class roomSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    building = serializers.CharField(max_length=100)
    owner = serializers.CharField(max_length=100)
    def create(self, validated_data):
        return addroom.objects.create(**validated_data)

##########Customer Account

class customeraccountSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    cnic = serializers.CharField(max_length=100)
    phno = serializers.IntegerField()
    role = serializers.CharField(max_length=100)
    address = serializers.CharField(max_length=100)
    room = serializers.CharField(max_length=100)
    rent = serializers.IntegerField()
    security = serializers.IntegerField()
    accountno = serializers.IntegerField()
    debt = serializers.IntegerField()
    def create(self, validated_data):
        return customeraccount.objects.create(**validated_data)

