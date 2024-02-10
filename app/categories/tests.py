from django.test import TestCase
from .models import Category

class CategoryModelTest(TestCase):

    def setUp(self):
        # Create a Category instance for testing
        self.category = Category.objects.create(name="Test Category", description="Test Description")

    def test_category_creation(self):
        # Test if the Category instance is created properly
        self.assertTrue(isinstance(self.category, Category))
        self.assertEqual(self.category.__str__(), "Test Category")

    def test_category_fields(self):
        # Test the field values of the Category instance
        category = Category.objects.get(id=self.category.id)
        self.assertEqual(category.name, "Test Category")
        self.assertEqual(category.description, "Test Description")

    def test_category_updated_field(self):
        # Test if 'updated' field is auto-updated on save
        old_updated_timestamp = self.category.updated
        self.category.description = "Updated Test Description"
        self.category.save()
        self.assertNotEqual(self.category.updated, old_updated_timestamp)

    def test_category_created_field(self):
        # Test if 'created' field is auto-set on creation and not updated on save
        old_created_timestamp = self.category.created
        self.category.name = "Updated Category Name"
        self.category.save()
        self.assertEqual(self.category.created, old_created_timestamp)

