from django.shortcuts import render

# Create your views here.
from rest_framework import generics
<<<<<<< HEAD
from rest_framework.authentication import TokenAuthentication
from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import IsAuthenticated

from .models import Doctor
from .serializer import DoctorSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
=======
from rest_framework.generics import ListCreateAPIView

from .models import Doctor
from .serializer import DoctorSerializer

>>>>>>> 5ddae3ea90fb26dfb6c9cd3b986eca70911470b3

# Create your views here.


class DoctorList(generics.ListCreateAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
<<<<<<< HEAD
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

=======
>>>>>>> 5ddae3ea90fb26dfb6c9cd3b986eca70911470b3


class DoctorDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
<<<<<<< HEAD
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

=======
>>>>>>> 5ddae3ea90fb26dfb6c9cd3b986eca70911470b3
