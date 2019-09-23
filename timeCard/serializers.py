from rest_framework import serializers
from . models import TimeCard


class TimeCardSerializer(serializers.ModelSerializer):

    class Meta:
        model = TimeCard
        fields = ('date', 'sector', 'location', 'time_in', 'daytime_in', 'time_out',
                  'daytime_out', 'hours_code', 'hours_worked')
