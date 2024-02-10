from django.test import TestCase
from unittest.mock import Mock
from .models import Category, Product, Report, ProblemReported

class CategoryModelTest(TestCase):
    def test_category_creation(self):
        category = Category.objects.create(name="Test Category", description="Test Description")
        self.assertEqual(category.name, "Test Category")
        self.assertEqual(category.description, "Test Description")

class ProductModelTest(TestCase):
    def test_product_creation(self):
        product = Product.objects.create(name="Test Product", description="Test Product Description", short_code="TP001")
        self.assertEqual(product.name, "Test Product")
        self.assertEqual(product.description, "Test Product Description")
        self.assertEqual(product.short_code, "TP001")


