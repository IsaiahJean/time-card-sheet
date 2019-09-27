from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Doctor(models.Model):
    first_Name = models.CharField(max_length=100)
    last_Name = models.CharField(max_length=100)
    file_number = models.PositiveIntegerField()
    pay_roll = models.CharField(max_length=3)


class Location(models.Model):
    sector = models.CharField(max_length=100)
    location = models.CharField(max_length=100)





