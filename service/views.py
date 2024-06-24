from django.shortcuts import render
from rest_framework import viewsets
from . import models
from . import serializers

class ServiceViewset(viewsets.ModelViewSet):
    queryset = models.Service.objects.all()
    serializer_class = serializers.ServiceSerializer