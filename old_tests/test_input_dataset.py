"""
Produce test for inputdataset correctly
"""

import unittest
import scripts.repo_first_script as rfs

class TestDatasetInput(unittest.TestCase):
    """
    Class to get the input dataset
    """

    def setUp(self):
        # Define a test dataset path
        self.test_dataset_path = 'datasets/FilmGenreStats.cwsv'

    def test_only_csvs_are_allowed(self):
        """
        Test that only csvs are allowed
        """
        with self.assertRaises(TypeError):
            rfs.load_dataset(self.test_dataset_path)


if __name__ == '__main__':
    unittest.main()
