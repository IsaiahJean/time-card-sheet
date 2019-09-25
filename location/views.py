from django.shortcuts import render

from rest_framework import generics
from rest_framework.generics import ListCreateAPIView

from .models import Location
from .serializer import LocationSerializer


# Create your views here.

class LocationList(generics.ListCreateAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
