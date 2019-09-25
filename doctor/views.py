from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from rest_framework.generics import ListCreateAPIView

from .models import Doctor
from .serializer import DoctorSerializer


# Create your views here.


class DoctorList(generics.ListCreateAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer


class DoctorDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
