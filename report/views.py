from .serializers import TimeCardSerializers
from rest_framework import generics

from timeCard.models import TimeCard


class PostReport (generics.ListAPIView):
    queryset = TimeCard.objects.all()
    serializer_class = TimeCardSerializers
