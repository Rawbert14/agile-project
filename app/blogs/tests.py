from django.test import TestCase
from django.contrib.auth.models import User
from .models import Category, Blog

class CategoryModelTests(TestCase):

    def setUp(self):
        Category.objects.create(category_name="Tech")

    def test_category_creation(self):
        category = Category.objects.get(category_name="Tech")
        self.assertEqual(category.category_name, "Tech")

    def test_category_str(self):
        category = Category.objects.get(category_name="Tech")
        self.assertEqual(str(category), "Tech")


class BlogModelTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        test_user = User.objects.create_user(username='testuser', password='12345')
        test_category = Category.objects.create(category_name="Tech")
        Blog.objects.create(
            title="Test Blog",
            category=test_category,
            author=test_user,
            short_description="This is a test blog short description.",
            blog_body="This is a test blog body.",
            status="Draft"
        )

    def test_blog_creation(self):
        blog = Blog.objects.get(title="Test Blog")
        self.assertEqual(blog.title, "Test Blog")
        self.assertEqual(blog.short_description, "This is a test blog short description.")
        self.assertEqual(blog.blog_body, "This is a test blog body.")
        self.assertEqual(blog.status, "Draft")

    def test_blog_str(self):
        blog = Blog.objects.get(title="Test Blog")
        self.assertEqual(str(blog), "Test Blog")
