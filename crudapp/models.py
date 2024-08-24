from django.db import models

# Create your models here.

class crStudent(models.Model):
    name = models.CharField(max_length=100, verbose_name='Student name')
    email = models.EmailField(max_length=200, verbose_name='Student Email')
    
    def __str__(self):
        return str(self.name)