from django.db import models

class users(models.Model):
    username=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
