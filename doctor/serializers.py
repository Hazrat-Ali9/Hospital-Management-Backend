from rest_framework import serializers
from . import models

class DoctorSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(many=False)
    designation = serializers.StringRelatedField(many=True)
    specialization = serializers.StringRelatedField(many=True)
    available_time = serializers.StringRelatedField(many=True)
    class Meta:
        model = models.Doctor
        fields = '__all__'
class SpecializationSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Specialization
        fields = '__all__'
        
class DesignationSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Designation
        fields = '__all__'
        
class AvailableTimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.AvailableTime
        fields = '__all__'
        
class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Review
        fields = '__all__'
