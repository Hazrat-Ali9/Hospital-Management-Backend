from django.shortcuts import render
from rest_framework import viewsets
from . import models
from . import serializers
# Create your views here.
class AppointmentViewSet(viewsets.ModelViewSet):
    queryset = models.Appointment.objects.all()
    serializer_class =  serializers.AppointmentSerializer
    
    # custom query kortechi
    def get_queryset(self):
        queryset = super().get_queryset() # 7 no line ke niye aslam ba patient ke inherit korlam
        print(self.request.query_params)
        patient_id = self.request.query_params.get('patient_id')
        if patient_id:
            queryset = queryset.filter(patient_id=patient_id)
        return queryset