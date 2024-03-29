from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from products.models import Product
from areas.models import ProductionLine
from categories.models import Category
from django.urls import reverse
import random
from django.db.models import Sum
from datetime import datetime
# Create your models here.

el = [
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 
    'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
    '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'
]
def random_code():
    random.shuffle(el)
    code = [str(x) for x in el[:12]]
    str_code = ''.join(code)
    return str_code

hours = ([(str(x), str(x)) for x in range(1,25)])


class ReportQueryset(models.QuerySet):
    def get_by_line_and_day(self, day, line_id):
        return self.filter(day=day, production_line__id=line_id)
    
    def aggregate_execution(self):
        return self.aggregate(Sum('execution'))
        
    def aggregate_plan(self):
        return self.aggregate(Sum('plan'))


class ReportManager(models.Manager):
    
    def get_queryset(self):
        return ReportQueryset(self.model, using=self._db)
    
    def get_by_line_and_day(self, day, line_id):
        return self.get_queryset().get_by_line_and_day(day, line_id)
    
    def aggregate_execution(self):
        return self.get_queryset().aggregate_execution()
        
    def aggregate_plan(self):
        return self.get_queryset().aggregate_plan()
    
    
class ProblemReportedManager(models.Manager):
    def get_problems_by_day_and_line(self, day, line):
        return super().get_queryset().filter(report__day = day, report__production_line__name = line)
    

class Report(models.Model):
    day = models.DateField(default=timezone.now)
    
    start_hour = models.TimeField()  
    end_hour = models.TimeField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    plan = models.PositiveIntegerField()
    execution = models.PositiveIntegerField()
    description = models.TextField(null=True, blank=True)
    production_line = models.ForeignKey(ProductionLine, on_delete=models.CASCADE)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    
    
    objects=ReportManager()
    
    def get_day(self):
        return self.day.strftime('%Y/%m/%d')
    
    def get_absolute_url(self):
        return reverse("reports:update-view", kwargs={"production_line": self.production_line, 'pk': self.pk,})
    
    
    def __str__(self):
        return "{}-{}-{}".format(self.start_hour, self.end_hour, self.production_line)
    
    class Meta:
        ordering = ('-created',)
        
        


    
class ProblemReported(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.TextField()
    problem_id = models.CharField(max_length=12, unique=True, blank=True, default=random_code)
    breakdown = models.PositiveIntegerField()
    public = models.BooleanField(default=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    report = models.ForeignKey(Report, on_delete=models.CASCADE)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    objects=ProblemReportedManager()
        
    def __str__(self):
        return "{}-{}".format(self.category.name, self.description[:20])
    
    class Meta:
        verbose_name = "Problem Reported"
        verbose_name_plural = "Problems Reported"

        
        
        
    
    