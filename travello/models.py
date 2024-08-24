from django.db import models

# Create your models here.

class destination(models.Model):

    name = models.CharField(max_length = 100)
    img = models.ImageField(upload_to='pics')
    desc = models.TextField()
    price = models.IntegerField()
    offer = models.BooleanField(default = False)
    
class news(models.Model):
    
    name = models.CharField(max_length=100)
    category = models.CharField(max_length = 100)
    desc = models.TextField()
    img = models.ImageField(upload_to='pics')
    date = models.DateTimeField()
    
class footer(models.Model):
    title = models.CharField(max_length=100)
    img = models.ImageField(upload_to='pics')
    address = models.CharField(max_length=100)
    number = models.CharField(max_length=100)
    
class slider(models.Model):
    img = models.ImageField(upload_to='pics')
    title = models.CharField(max_length=100)
    
class Newslettersubscribsion(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique = True)
    
    def __str__(self):
        return self.email
    
class travel_cnt(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(max_length=50)
    number=models.CharField(max_length=20)
    address=models.TextField(max_length=200)