from django.contrib import admin
from .models import GeneralPost, ProblemPost, Comment
# Register your models here.

admin.site.register(GeneralPost)
admin.site.register(ProblemPost)
admin.site.register(Comment)
