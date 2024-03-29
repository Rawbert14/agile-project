from django.db import models
from profiles.models import Profile
from products.models import Product
# Create your models here.


class ProductionLine(models.Model):
    name = models.CharField(max_length=200)
    team_leader = models.ForeignKey(Profile, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    description = models.CharField(
        max_length=500, default='Not a description yet')

    def __str__(self):
        return self.name
