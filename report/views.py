from .serializers import TimeCardSerializers
from rest_framework import generics

from timeCard.models import TimeCard
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


class PostReport (generics.ListAPIView):
    queryset = TimeCard.objects.all()
    serializer_class = TimeCardSerializers
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

