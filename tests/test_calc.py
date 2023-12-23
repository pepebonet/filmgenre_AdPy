"""
Sctipt to test calc.py
"""

import scripts.calc as ca


def test_sum():
    """
    Function to test sum
    """
    result = ca.sum_numbers(5, 10)

    assert result == 15


def test_substract():
    """
    Function to test sum
    """
    result = ca.substract_numbers(5, 10)

    assert result == -5
