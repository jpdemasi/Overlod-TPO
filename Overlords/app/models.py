from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=20)
    mail = models.EmailField()
    phone = models.CharField(max_length=15)
    text = models.CharField(max_length=160)
    password = models.CharField(max_length=20, null=False, default="none")