import json
import random
from hashlib import md5

from django.shortcuts import render

# Create your views here.
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import User, POIVisit


class POIVisitSerializer(serializers.ModelSerializer):
    class Meta:
        model = POIVisit
        fields = ['poi_id', 'latitude', 'longitude', 'visit_count']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'phone_id']


class UserDetail(APIView):
    def get(self, request, pk):
        serialize = UserSerializer(User.objects.get(pk=pk))
        return Response(status=200, data=serialize.data)


class UserList(APIView):
    def get(self, request):
        serialize = UserSerializer(User.objects.all(), many=True)
        return Response(status=200, data=serialize.data)


class GetPOIVisitByIds(APIView):
    def get(self, request):
        user_id = request.GET.get('uid', None)
        poi_id = request.GET.get('poi_id', None)

        if None in [poi_id, user_id]:
            return Response(status=400, data="Missing request parameters.")

        try:
            user = User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return Response(status=400, data="User not found.")

        try:
            poi = POIVisit.objects.get(user=user, poi_id=poi_id)
        except POIVisit.DoesNotExist:
            poi = POIVisit()
            poi.poi_id = poi_id
            poi.visit_count = 0

        return Response(status=200, data=POIVisitSerializer(poi).data)


class GetPOIVisits(APIView):
    def get(self, request):
        user_id = request.GET.get('uid', None)
        num = int(request.GET.get('num', 10))

        if None in [user_id]:
            return Response(status=400, data="uid is null.")

        try:
            user = User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return Response(status=400, data="User not found.")

        pois = POIVisitSerializer(POIVisit.objects.filter(user=user).order_by("-visit_count")[:num], many=True)

        return Response(status=200, data=pois.data)


class VisitPOI(APIView):
    def post(self, request):
        js = json.loads(request.body)
        user_id = js.get('uid', None)
        poi_id = js.get('poi_id', None)
        latitude = js.get('latitude', None)
        longitude = js.get('longitude', None)

        # TODO: Security concerns.
        time = request.POST.get('time', None)
        secret = request.POST.get('secret', None)

        if None in [user_id, poi_id, latitude, longitude]:
            return Response(status=400, data="Missing request params.")

        try:
            user = User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return Response(status=400, data="User not found.")

        try:
            poi_visit = POIVisit.objects.get(user=user, poi_id=poi_id)
            poi_visit.visit_count += 1
        except POIVisit.DoesNotExist:
            poi_visit = POIVisit()
            poi_visit.poi_id = poi_id
            poi_visit.longitude = longitude
            poi_visit.latitude = latitude
            poi_visit.user = user
            poi_visit.visit_count = 1

        poi_visit.save()

        return Response(status=200, data="Success")


class DummyUser(APIView):
    def get(self, request, num):
        for i in range(num):
            User.save(User(phone_id=md5(('%.f' % random.random()).encode('utf-8')).hexdigest()))
        return Response("Success")
