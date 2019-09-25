from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Doctor(models.Model):
    first_Name = models.ForeignKey(User, related_name='Doctor', on_delete=models.CASCADE)
    last_Name = models.ForeignKey(User, on_delete=models.CASCADE)
    file_number = models.PositiveIntegerField()
    pay_roll = models.CharField(max_length=3)


class Location(models.Model):
    sector = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    file_number = models.ForeignKey(Doctor, on_delete=models.CASCADE)




