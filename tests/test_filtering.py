"""
Test filtering the dataset
"""
import unittest
import pandas as pd
from scripts.filtering import FilteringClass


class TestFiltering(unittest.TestCase):
    """
    Class to test the filters on the dataset
    """

    def test_filtering_price(self):
        """
        Test the price filtering in the dataset
        """

        df = pd.DataFrame({"Price Starting With ($)": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]})
        result = FilteringClass(df).filter_price(5)
        self.assertEqual(result.shape[0], 4)

    def test_filtering_price_high(self):
        """
        Test the price filtering in the dataset
        """

        df = pd.DataFrame({"Price Starting With ($)": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]})
        result = FilteringClass(df).filter_price_high(5)
        self.assertEqual(result.shape[0], 5)


if __name__ == "__main__":
    unittest.main()
