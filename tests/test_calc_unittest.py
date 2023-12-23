"""
Test calc script with unittest
"""

import unittest
import scripts.calc as ca


class TestCalcScript(unittest.TestCase):
    """
    Class to test the Calc Script
    """

    def test_add(self):
        """
        Test for the sum function
        """

        result = ca.sum_numbers(10, 5)
        self.assertEqual(result, 15)

    def test_substract(self):
        """
        Test for the substract function
        """

        result = ca.substract_numbers(10, 5)
        self.assertEqual(result, 5)