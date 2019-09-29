from django.shortcuts import render

from rest_framework import generics
from rest_framework.generics import ListCreateAPIView

from .models import Location
from .serializer import LocationSerializer
<<<<<<< HEAD
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
=======

>>>>>>> 5ddae3ea90fb26dfb6c9cd3b986eca70911470b3

# Create your views here.

class LocationList(generics.ListCreateAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
<<<<<<< HEAD
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

=======
>>>>>>> 5ddae3ea90fb26dfb6c9cd3b986eca70911470b3
