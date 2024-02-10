from django.test import TestCase
from .models import ProductionLine

class ProductionLineModelTest(TestCase):

    def test_production_line_name(self):
        production_line = ProductionLine(name="Line 1")
        self.assertEqual(production_line.name, "Line 1")

    def test_production_line_description_default(self):
        production_line = ProductionLine(name="Line 2")
        self.assertEqual(production_line.description, 'Not a description yet')

    def test_production_line_str_representation(self):
        production_line = ProductionLine(name="Test Production Line")
        self.assertEqual(str(production_line), "Test Production Line")
