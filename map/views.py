import random

from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import serializers, status

from user.models import User
from user.views import UserSerializer
from .models import Location


class LocationSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    user_id = serializers.PrimaryKeyRelatedField(
        write_only=True,
        queryset=User.objects.all(),
        source='user'
    )

    class Meta:
        model = Location
        fields = ['id', 'user_id', 'user', 'latitude', 'longitude', 'latitude_precise', 'longitude_precise']

    def create(self, validated_data):
        return Location.objects.create(**validated_data)


class AddLocation(APIView):
    def post(self, request):
        location = LocationSerializer(data=request.data)
        print(location)
        if location.is_valid():
            location.save()
            return Response(location.data, status=status.HTTP_201_CREATED)
        else:
            return Response(location.data, status=status.HTTP_400_BAD_REQUEST)


# Create your views here.
class LocationList(APIView):
    def get(self, request, uid):
        locations = Location.objects.filter(user_id=uid, delete=False)
        serialize = LocationSerializer(locations, many=True)
        return Response(serialize.data)


class DummyLocationUser(APIView):
    def get(self, request, uid, num):
        for i in range(num):
            latitude_num = (random.random() * 100)
            longitude_num = (random.random() * 100)

            location = Location()

            location.latitude_precise = '%.7f' % latitude_num
            location.longitude_precise = '%.7f' % longitude_num
            location.latitude = '%.2f' % latitude_num
            location.longitude = '%.2f' % longitude_num

            location.user = User.objects.get(id=uid)

            Location.save(location)

        return Response("Success")


class DummyLocation(APIView):
    def get(self, request, num):
        for i in range(num):
            latitude_num = (random.random() * 100)
            longitude_num = (random.random() * 100)

            location = Location()

            location.latitude_precise = '%.7f' % latitude_num
            location.longitude_precise = '%.7f' % longitude_num
            location.latitude = '%.2f' % latitude_num
            location.longitude = '%.2f' % longitude_num
            users = User.objects.all()
            location.user = users[random.randrange(len(users))]
            Location.save(location)

        return Response("Success")
