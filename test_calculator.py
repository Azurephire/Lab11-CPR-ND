# https://github.com/Azurephire/Lab11-CPR-ND
# Partner 1: Nicholas Di Grazia
# Partner 2: Camila Perez Ramirez

import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    def test_add(self): # 3 assertions
        self.assertEqual(add(5, 4), 9)
        self.assertEqual(add(-18, 5),-13)
        self.assertEqual(add(-11, -5), -16)

    def test_subtract(self): # 3 assertions
        self.assertEqual(subtract(7, 5), 2)
        self.assertEqual(subtract(-8, 3), -11)
        self.assertEqual(subtract(-9, -3), -6)
    ##########################

    ######## Partner 1
    def test_multiply(self): # 3 assertions
        self.assertEqual(mul(2, 5), 10)
        self.assertEqual(mul(15,3), 45)
        self.assertEqual(mul(10, 10), 100)
    def test_divide(self): # 3 assertions
        self.assertEqual(div(2, 10), 5)
        self.assertEqual(div(5, 30), 6)
        self.assertEqual(div(10, 100), 10)


    ######## Partner 2
    def test_divide_by_zero(self): # 1 assertion
        # call division function inside, example:
        # with self.assertRaises(<INSERT_ERROR_TYPE>):
        #     div(0, 5)
        with self.assertRaises(ZeroDivisionError):
            div(0, 11)

    def test_logarithm(self): # 3 assertions
        self.assertEqual(logarithm(5, 1), 0)
        self.assertEqual(logarithm(3, 9), 2)
        self.assertEqual(logarithm(2, 64), 6)

    def test_log_invalid_base(self): # 1 assertion
        # use same technique from test_divide_by_zero
        with self.assertRaises(ValueError):
            logarithm(7, 0)
    ##########################
    
    ######## Partner 1
    def test_log_invalid_argument(self): # 1 assertion
        with self.assertRaises(ValueError):
            logarithm(7, 0)

    def test_hypotenuse(self): # 3 assertions
        self.assertAlmostEqual(hypotenuse(3, 5), math.sqrt(34))
        self.assertAlmostEqual(hypotenuse(4, 5), math.sqrt(41))
        self.assertAlmostEqual(hypotenuse(5, 5), math.sqrt(50))

    def test_sqrt(self): # 3 assertions
        self.assertEqual(square_root(25), 5)
        self.assertEqual(square_root(36), 6)
        self.assertEqual(square_root(100), 10)

# Do not touch this
if __name__ == "__main__":
    unittest.main()