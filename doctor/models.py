from django.db import models

# Create your models here.
class Doctor(models.Model):
    first_Name = models.CharField(max_length=100)
    last_Name = models.CharField(max_length=100)
<<<<<<< HEAD
    file_number = models.PositiveIntegerField()
    pay_roll = models.CharField(max_length=3)
=======
    pay_roll = models.CharField(max_length=4)
>>>>>>> 5ddae3ea90fb26dfb6c9cd3b986eca70911470b3
