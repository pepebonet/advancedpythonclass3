import unittest
import pandas as pd
from scripts.repo_first_script import FilteringClass

class TestFilteringClass(unittest.TestCase):

    def setUp(self):
        self.sample_data = {
            'Price Starting With ($)': [10, 15, 8, 20],
            # Add other columns as needed for your DataFrame
        }

    def test_filter_price(self):
        df = pd.DataFrame(self.sample_data)
        result = FilteringClass(df).filter_price(12)
        self.assertEqual(result.shape, (2, 1))  # Adjust the shape based on your expected output


if __name__ == "__main__":
    unittest.main()
