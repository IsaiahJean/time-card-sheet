from rest_framework import serializers
from doctor.models import Doctor
from timeCard.models import TimeCard


class DoctorSerializers(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = '__all__'


class TimeCardSerializers(serializers.ModelSerializer):
    file_number = DoctorSerializers()

    class Meta:
        model = TimeCard
        fields = '__all__'
