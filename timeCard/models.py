from django.db import models
from doctor.models import Doctor
# Create your models here.


class TimeCard(models.Model):
    file_number = models.ForeignKey(Doctor, on_delete=models.CASCADE)  # Connected with Doctors table
    date = models.CharField(max_length=100)  # Current Date
    sector = models.CharField(max_length=5)  # West or East
    location = models.CharField(max_length=15)
    time_in = models.CharField(max_length=10)
    time_out = models.CharField(max_length=10)
    hours_code = models.CharField(max_length=4)  # FBP/AMCO
    hours_worked = models.CharField(max_length=10)  # Calculated from Time in and Time out values
