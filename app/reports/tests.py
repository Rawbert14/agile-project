from django.test import TestCase
from profiles.models import Profile
from products.models import Product
from .models import ProductionLine
from django.contrib.auth.models import User

class ProductionLineModelTest(TestCase):
    def setUp(self):
        self.team_leader = Profile.objects.create(user=User.objects.create_user(username='teamleader', password='testpass'), bio='Team Leader Bio', team='Test Team Leader')
        self.production_line = ProductionLine.objects.create(name='Test Line', team_leader=self.team_leader)

        # Create some products for testing
        self.product1 = Product.objects.create(name='Product 1')
        self.product2 = Product.objects.create(name='Product 2')

        # Add products to the production line
        self.production_line.products.add(self.product1, self.product2)
        
        

    def test_production_line_creation(self):
        self.assertEqual(self.production_line.name, 'Test Line')
        self.assertEqual(self.production_line.team_leader, self.team_leader)

    def test_production_line_str(self):
        self.assertEqual(str(self.production_line), 'Test Line')

    def test_production_line_products(self):
        self.assertIn(self.product1, self.production_line.products.all())
        self.assertIn(self.product2, self.production_line.products.all())
