from django.contrib import admin
from . import models
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
# Register your models here.

class AppointmentAdmin(admin.ModelAdmin):
    list_display = ['doctor_name', 'patient_name', 'appointment_types', 'appointment_status', 'symptom', 'time', 'cancel']
    def patient_name(self,obj):
        return obj.patient.user.first_name
    
    def doctor_name(self,obj):
        return obj.doctor.user.first_name
    
    def save_model(self, request, obj, form, change):
        obj.save()
        if obj.appointment_status == "Running" and obj.appointment_types == "Online":
            email_subject = "Your Online Appointment is Running"
            email_body = render_to_string('admin_email.html', {'user' : obj.patient.user, 'doctor' : obj.doctor})
            
            email = EmailMultiAlternatives(email_subject , '', to=[obj.patient.user.email])
            email.attach_alternative(email_body, "text/html")
            email.send()
    
admin.site.register(models.Appointment, AppointmentAdmin)