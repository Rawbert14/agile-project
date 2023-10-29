from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    short_code = models.CharField(max_length=200)
    updated = models.TimeField(auto_now=True) 
    created = models.TimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name