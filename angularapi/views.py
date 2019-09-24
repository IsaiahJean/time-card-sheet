from django.shortcuts import render

from rest_framework import generics
from rest_framework.generics import ListCreateAPIView

from .models import Doctor, Location
from .serializer import DoctorSerializer, LocationSerializer


# Create your views here.

class LocationList(generics.ListCreateAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer


class DoctorList(generics.ListCreateAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer


class DoctorDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
