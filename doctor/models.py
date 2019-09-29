from django.db import models

# Create your models here.
class Doctor(models.Model):
    first_Name = models.CharField(max_length=100)
    last_Name = models.CharField(max_length=100)

    

    pay_roll = models.CharField(max_length=4)


 
