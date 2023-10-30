from django.db import models
from profiles.models import Profile
from reports.models import Report, ProblemReported
from django.core.validators import FileExtensionValidator
# Create your models here.

class Post(models.Model):
    author = models.ForeignKey(Profile, on_delete=models.CASCADE)
    liked = models.ManyToManyField(Profile, related_name="liked")
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    
    @property
    def num_likes(self):
        return self.liked.all().count()
        
    

class ProblemPost(Post):
    report = models.ForeignKey(Report, on_delete=models.CASCADE)
    problem_reported = models.ForeignKey(ProblemReported, on_delete=models.CASCADE)
    
    def __str__(self):
        return "{}".format(self.problem_reported.description)[:50]
        
    
    
class GeneralPost(Post):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=300)
    image = models.ImageField(blank=True, validators=[FileExtensionValidator(['png','jpg', 'jpeg'])])
    
    def __str__(self):
        return str(self.title)

