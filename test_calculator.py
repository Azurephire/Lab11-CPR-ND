import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    # def test_add(self): # 3 assertions
    #     fill in code

    # def test_subtract(self): # 3 assertions
    #     fill in code
    # ##########################

    ######## Partner 1
    def test_multiply(self): # 3 assertions
        self.assertEqual(mul(2, 5), 10)
        self.assertEqual(mul(15,3), 45)
        self.assertEqual(mul(10, 10), 100)
    def test_divide(self): # 3 assertions
        self.assertEqual(div(2, 10), 5)
        self.assertEqual(div(5, 30), 6)
        self.assertEqual(div(100, 10), 10)


    ######## Partner 2
    # def test_divide_by_zero(self): # 1 assertion
    #     # call division function inside, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #     div(0, 5)
    #     fill in code

    # def test_logarithm(self): # 3 assertions
    #     fill in code

    # def test_log_invalid_base(self): # 1 assertion
    #     # use same technique from test_divide_by_zero
    #     fill in code
    # ##########################
    
    ######## Partner 1
    def test_log_invalid_argument(self): # 1 assertion
        with self.assertRaises(ValueError):
            logarithm(7, 0)




    def test_hypotenuse(self): # 3 assertions
        self.assertAlmostEqual(hypotenuse(3, 5), math.sqrt(34))
        self.assertAlmostEqual(hypotenuse(4, 5), math.sqrt(41))
        self.assertAlmostEqual(hypotenuse(5, 5), math.sqrt(50))

    def test_sqrt(self): # 3 assertions
        with self.assertRaises(ValueError):
            self.assertEqual(square_root(25), 5)
            self.assertEqual(square_root(36), 6)
            self.assertEqual(square_root(100), 10)

# Do not touch this
if __name__ == "__main__":
    unittest.main()