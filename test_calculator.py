from calculator import *
import unittest

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    # def test_add(self): # 3 assertions
    #     fill in code

    # def test_subtract(self): # 3 assertions
    #     fill in code
    # ##########################

    ####### Partner 1
    def test_multiply(self): # 3 assertions
        self.assertEqual(4 *25 , mul(4, 25))
        self.assertEqual(-30 * 5, mul(-30, 5))
        self.assertEqual(0 * 5, mul(0, 5))
        self.assertEqual(123456789 * 123456789, mul(123456789, 123456789))
    def test_divide(self): # 3 assertions
        self.assertEqual(25/5, div(5,25))
        self.assertEqual(-30 / 6, div(6, -30))
        self.assertEqual(35 / -3, div(-3, 35))
        with self.assertRaises(ZeroDivisionError):
            self.assertEqual(25 / 0, div(0, 25))

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
    
    ####### Partner 1
    def test_log_invalid_argument(self): # 1 assertion
        # call log function inside, example:
        with self.assertRaises(ValueError):
            logarithm(0, 5)
            logarithm(6,0)
            logarithm(9999, 0)
#test

    def test_hypotenuse(self): # 3 assertions
        self.assertEqual(5, hypotenuse(3,4))
        self.assertAlmostEqual(10.81665, hypotenuse(6, 9))
        self.assertEqual(5, hypotenuse(-3, -4))
    def test_sqrt(self): # 3 assertions
        # Test for invalid argument, example:
        with self.assertRaises(TypeError):
           square_root("four")
        with self.assertRaises(ValueError):
           square_root(-4)



# Do not touch this
if __name__ == "__main__":
    unittest.main()