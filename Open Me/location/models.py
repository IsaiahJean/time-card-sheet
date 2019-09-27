from django.db import models


# Create your models here.
class Location(models.Model):
    sector = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
