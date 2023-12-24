"""
Tests for inputting the right dataset
"""

import unittest
import numpy as np
import pandas as pd
import scripts.explore_dataset as ed


class DatasetInput(unittest.TestCase):
    """
    Class for testing the input dataset
    """

    def test_only_csvs_are_allowed(self):
        """
        Test that only csvs are allowed
        """

        with self.assertRaises(TypeError):
            ed.load_dataset('datasets/FilmGenreStats.cwsv')

    def test_dataset_dimensions(self):
        """
        Test number of columns and rows of the dataset
        """

        df = pd.DataFrame(
            np.random.rand(100001, 5),
            columns=['A', 'B', 'C', 'D', 'E']
        )

        with self.assertRaises(ValueError):
            ed.check_columns(df)
