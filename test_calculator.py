import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(1, 2), 3)

    # Add the following test methods to the TestCalculator class:
    def test_add_neg(self):
        self.assertEqual(self.calc.add(-1, -2), -3)

    def test_sub(self):
        self.assertEqual(self.calc.subtract(3, 2), 1)

    def test_sub_neg(self):
        self.assertEqual(self.calc.subtract(2, -3), 5)

    def test_mul(self):
        self.assertEqual(self.calc.multiply(3, 2), 6)

    def test_mul_zero(self):
        self.assertEqual(self.calc.multiply(3, 0), 0)
    
    def test_div(self):
        self.assertEqual(self.calc.divide(4, 2), 2)
    
    def test_div_remain(self):
        self.assertEqual(self.calc.divide(9, 4), 2)
    
    def test_mod(self):
        self.assertEqual(self.calc.modulo(3, 2), 1)

    def test_mod_self(self):
        self.assertEqual(self.calc.modulo(3, 3), 0)
        
if __name__ == '__main__':
    unittest.main()