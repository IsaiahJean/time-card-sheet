from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# Description model, user - foreign key from auth_user django table
class UserDescription(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.CharField(max_length=40)
