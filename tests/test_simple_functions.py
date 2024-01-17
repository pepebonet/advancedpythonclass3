"""
Script to write the test for the sum and subtract functions
"""
import unittest
import numpy as np
import scripts.simple_functions as sf

# from scripts.simple_functions import sum_two_nums, sub_two_nums


class TestSimpleFunctions(unittest.TestCase):
    """
    Test simple functions sum & subtract
    """

    def test_sum(self):
        """
        Test the sum function
        """
        result = sf.sum_two_nums(4, 5)
        self.assertEqual(result, 9)

    def test_sub(self):
        """
        Test the sub function
        """
        result = sf.sub_two_nums(1, 3)
        self.assertEqual(result, -2)

        for i in range(100):
            a = np.round(np.random.random(1), 2)
            b = np.round(np.random.random(1), 2)
            result = sf.sub_two_nums(a, b)
            self.assertEqual(result, a - b)


if __name__ == "__main__":
    unittest.main()
