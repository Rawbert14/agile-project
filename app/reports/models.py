from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from products.models import Product
from areas.models import ProductionLine
# Create your models here.

hours = ([(str(x), str(x)) for x in range(1,25)])

class Report(models.Model):
    day = models.DateField(default=timezone.now)
    start_hour = models.CharField(max_length=200, choices=hours)
    end_hour = models.CharField(max_length=200, choices=hours)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    plan = models.PositiveIntegerField()
    execution = models.PositiveIntegerField()
    production_line = models.ForeignKey(ProductionLine, on_delete=models.CASCADE)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return "{}-{}-{}".format(self.start_hour, self.end_hour, self.production_line)
    
    