from django.db import models

# Create your models here.


class TimeCard(models.Model):
    date = models.DateField()  # Current Date
    sector = models.CharField(max_length=5)  # West or East
    location = models.CharField(max_length=15)
    time_in = models.TimeField()
    daytime_in = models.CharField(max_length=2)  # AM/PM
    time_out = models.TimeField()
    daytime_out = models.CharField(max_length=2)  # AM/PM
    hours_code = models.CharField(max_length=4)  # FBP/AMCO
    hours_worked = models.DecimalField(max_digits=4, decimal_places=0)  # Calculated from Time in and Time out values
