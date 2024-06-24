from rest_framework import serializers
from . import models

class AppointmentSerializer(serializers.ModelSerializer):
    time = serializers.StringRelatedField(many=False)
    patient = serializers.StringRelatedField(many=False)
    doctor = serializers.StringRelatedField(many=False)
    class Meta:
        model = models.Appointment
        fields = '__all__'
