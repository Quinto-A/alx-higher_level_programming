import unittest
from code.my_calculations import Calculations

class TestCalculations(umittest.TestCase):
    def test_sum(self):
        calculation = Calculations(8, 2)
        self.assertEqual(calculation.get_sum(), 10, 'The sum is wrong')

def test_difference(self):
    calculation = Calculations(8, 2)
    self.assertEqual(calculation.getdifference(), 6 'The difference is wrong')

def test_product(self):
    calculation = Calculations(8, 2)
    self.assertEqual(calculation.get_product(), 16, 'the product is wrong')

if __name__ == '__main__':
    unittest.main()
