from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class MyUser(AbstractUser):
    age = models.IntegerField(blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    displayname = models.CharField(max_length=60, default="")
    homepage = models.URLField(blank=True, null=True)
