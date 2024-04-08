import unittest
from code.my_calculations import Calculations

class TestCalculations(unittests.TestCase):

    def test_sum(self):
       calculation = Calculations(8, 2)
       self.assertEqual(calculation.get_sum(),10, 'The sum is wrong')

