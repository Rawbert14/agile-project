from django.test import TestCase
from django.contrib.auth.models import User
from profiles.models import Profile
from products.models import Product
from .models import ProductionLine

class ProductionLineModelTest(TestCase):

    def setUp(self):
        # Check if a user with username 'teamleader' already exists
        try:
            self.user = User.objects.get(username='teamleader')
        except User.DoesNotExist:
            # If not, create a new user
            self.user = User.objects.create_user(username='teamleader', password='testpassword')

        # Create a profile for the team leader
        self.team_leader_profile, created = Profile.objects.get_or_create(user=self.user, defaults={'bio': 'Team Leader Bio', 'team': 'Team Leader Team'})

        # Create a product
        self.product = Product.objects.create(name='Test Product', description='Test Description', short_code='TP1')

        # Create a production line with a team leader and a product
        self.production_line = ProductionLine.objects.create(
            name='Test Production Line',
            team_leader=self.team_leader_profile,
        )
        self.production_line.products.add(self.product)

    def test_production_line_creation(self):
        self.assertEqual(self.production_line.name, 'Test Production Line')
        self.assertEqual(self.production_line.team_leader, self.team_leader_profile)
        self.assertEqual(list(self.production_line.products.all()), [self.product])

    def test_production_line_str_representation(self):
        expected_str = self.production_line.name
        self.assertEqual(str(self.production_line), expected_str)
