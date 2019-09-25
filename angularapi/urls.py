
from django.contrib import admin
from django.conf.urls import url, include
from .views import DoctorList,DoctorDetail, LocationList

urlpatterns = [

    url(r'locations/', LocationList.as_view(), name="location_list"),
    url(r'doctors/', DoctorList.as_view(), name="doctor_list"),
    url(r'doctors/<int:pk>/', DoctorDetail.as_view(), name="doctor_detail"),

]