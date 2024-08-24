from django.db import models

# Create your models here.

class add_students(models.Model):
    roll = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    address = models.TextField(max_length=250)
    phone = models.CharField(max_length=20)
  