from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Category(models.Model):
    category_name = models.CharField(max_length=200, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name_plural = 'Categories'
        
    def __str__(self):
        return self.category_name
    
STATUS_CHOICES=(
    ('Draft', 'Darft'),
    ('Published', 'Published')
)  

class Blog(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=250, unique=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    short_description =models.TextField(max_length=500)
    description = models.TextField(blank=True, null=True)
    blog_body = models.TextField(max_length=5000)
    status = models.CharField(max_length=20, choices= STATUS_CHOICES, default='Draft')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    
    def __str__(self):
        return self.title
