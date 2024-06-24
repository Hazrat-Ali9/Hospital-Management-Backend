from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter() # wifi toiri korlam
router.register('', views.AppointmentViewSet) # ekta entena toiri korlam

urlpatterns = [
    path('', include(router.urls)),
]

