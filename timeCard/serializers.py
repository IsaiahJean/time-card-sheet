from rest_framework import serializers
from . models import TimeCard


class TimeCardSerializer(serializers.ModelSerializer):

    class Meta:
        model = TimeCard
        fields = '__all__'
