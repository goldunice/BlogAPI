from rest_framework import serializers
from .models import *


class MuallifSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    ism = serializers.CharField()
    yosh = serializers.IntegerField()
    kasb = serializers.CharField()
    username = serializers.CharField()
    password = serializers.IntegerField()


class MaqolaSerialzier(serializers.ModelSerializer):
    class Meta:
        model = Maqola
        fields = "__all__"
