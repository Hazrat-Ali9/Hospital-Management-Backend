from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from . import models
from . import serializers
# Create your views here.
class AppointmentViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = models.Appointment.objects.all()
    serializer_class =  serializers.AppointmentSerializer

    # Restrict results to the authenticated user own appointments
    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(patient__user=self.request.user)
        patient_id = self.request.query_params.get("patient_id")
        if patient_id:
            queryset = queryset.filter(patient_id=patient_id)
        return queryset
