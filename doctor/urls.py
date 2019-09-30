from django.contrib import admin
from django.conf.urls import url, include
from .views import DoctorList, DoctorDetail
from django.urls import path

urlpatterns = [

    path(r'', DoctorList.as_view(), name="doctor_list"),
    path(r'<int:pk>/', DoctorDetail.as_view(), name="doctor_detail"),

]