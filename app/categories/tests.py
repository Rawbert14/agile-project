import datetime
from django.test import TestCase
from .models import Category

class CategoryModelTest(TestCase):

    def setUp(self):
        self.category = Category.objects.create(
            name="Test Category",
            description="Test Description"
        )

    def test_category_creation(self):
        self.assertEqual(self.category.name, "Test Category")
        self.assertEqual(self.category.description, "Test Description")

    def test_category_str_representation(self):
        self.assertEqual(str(self.category), "Test Category")

    def test_verbose_names(self):
        self.assertEqual(Category._meta.verbose_name, "Category")
        self.assertEqual(Category._meta.verbose_name_plural, "Categories")

    def test_created_and_updated_fields(self):
        # Check if created and updated fields are set correctly
        self.assertIsNotNone(self.category.created)
        self.assertIsNotNone(self.category.updated)

        # Check if created and updated fields are datetime objects
        self.assertIsInstance(self.category.created, datetime.datetime)
        self.assertIsInstance(self.category.updated, datetime.datetime)
