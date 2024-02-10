from django.test import TestCase
from .models import Product

class ProductModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        Product.objects.create(
            name='Test Product',
            description='This is a test product',
            short_code='TP'
        )

    def test_name_max_length(self):
        product = Product.objects.get(id=1)
        max_length = product._meta.get_field('name').max_length
        self.assertEquals(max_length, 200)

    def test_description_blank(self):
        product = Product.objects.get(id=1)
        field = product._meta.get_field('description')
        self.assertTrue(field.blank)
        self.assertTrue(field.null)

    def test_short_code_max_length(self):
        product = Product.objects.get(id=1)
        max_length = product._meta.get_field('short_code').max_length
        self.assertEquals(max_length, 200)

    def test_updated_auto_now(self):
        product = Product.objects.get(id=1)
        self.assertIsNotNone(product.updated)

    def test_created_auto_now_add(self):
        product = Product.objects.get(id=1)
        self.assertIsNotNone(product.created)

    def test_str_method(self):
        product = Product.objects.get(id=1)
        self.assertEqual(str(product), 'Test Product')
        

    def setUp(self):
        # Create a Product instance to use in tests
        self.product = Product.objects.create(
            name='Test Product',
            description='Test Description',
            short_code='TP001'
        )

    def test_product_creation(self):
        # Test that the Product instance was created properly
        self.assertEqual(self.product.name, 'Test Product')
        self.assertEqual(self.product.description, 'Test Description')
        self.assertEqual(self.product.short_code, 'TP001')

    def test_product_string_representation(self):
        # Test the string representation of the Product model
        self.assertEqual(str(self.product), 'Test Product')

