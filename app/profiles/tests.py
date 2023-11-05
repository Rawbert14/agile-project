from django.test import TestCase
from django.contrib.auth.models import User
from .models import Profile, get_upload_path

class ProfileModelTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser1', password='testpassword1')

    def test_get_upload_path(self):
        filename = 'test.jpg'
        upload_path = get_upload_path(None, filename)
        self.assertTrue(upload_path.startswith('uploads/profile/img/'))
        self.assertTrue(upload_path.endswith('.jpg'))

