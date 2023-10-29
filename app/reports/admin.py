from django.contrib import admin
from .models import ProblemReported, Report

# Register your models here.

admin.site.register(Report)
admin.site.register(ProblemReported)
