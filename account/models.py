from django.db import models
from django.db.models.base import Model

# Create your models here.
class Register(models.Model):
    first_name = models.CharField(max_length=50, null=False)
    last_name = models.CharField(max_length=65, null=False)
    username = models.CharField(max_length=65, unique=True, null=False)
    password = models.CharField(max_length=200, null=False)


class Login(models.Model):
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)

