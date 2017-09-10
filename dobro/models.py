from django.db import models


class Profile(models.Model):
    login = models.CharField(max_length=20, unique=True)
    password = models.CharField(max_length=256)
    email = models.CharField(max_length=30, unique=True)
    vk = models.BigIntegerField(null=True)
    fb = models.BigIntegerField(null=True)