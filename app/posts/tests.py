from django.test import TestCase
from django.contrib.auth.models import User
from .models import GeneralPost, ProblemPost
from profiles.models import Profile
from reports.models import Report, ProblemReported

class GeneralPostModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testingtoseeifworks', password='testsspassss')
        self.profile = Profile.objects.create(user=self.user, bio='Test Bio', team='Test Team')
        self.post = GeneralPost.objects.create(author=self.profile, title='Test Title', description='Test Description')
        
        

    def test_general_post_creation(self):
        self.assertEqual(self.post.title, 'Test Title')
        self.assertEqual(self.post.description, 'Test Description')

