import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()
    # Addition
    def test_add_1(self):
        self.assertEqual(self.calc.add(-1, -2), -3)
    def test_add_2(self):
        self.assertEqual(self.calc.add(-1, 3), 2)
    
    # Subtraction
    def test_sub_1(self) :
        self.assertEqual(self.calc.subtract(-10, 7), -17)
    def test_sub_2(self) :
        self.assertEqual(self.calc.subtract(-5, -2), -3)

    # Multiply
    def test_mul_1(self) :
        self.assertEqual(self.calc.multiply(6, 5), 30)
    def test_mul_2(self) :
        self.assertEqual(self.calc.multiply(4, -3), -12)

    # Divide
    def test_div_1(self) :
        self.assertEqual(self.calc.divide(-6, 5), -1)
    def test_div_2(self) :
        self.assertEqual(self.calc.divide(-10, -5), 2)

    # Modulo
    def test_mod_1(self) :
        self.assertEqual(self.calc.modulo(1, -5), -4)
    def test_mod_2(self) :
        self.assertEqual(self.calc.modulo(-9, -3), 0)


    # Add the following test methods to the TestCalculator class:

if __name__ == '__main__':
    unittest.main()