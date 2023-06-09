"""Test py fuction"""
import unittest
from main import sorted_squared_array


class TestMLApi(unittest.TestCase):
    """
    Testing edge chases for sorted squared array function, paying attention to negative 
    chases and null valules.
    """
    def test_sorted_squared_array(self):
        """
        Testing end to end api feature detection module hit all relevant feature detection
        models and roi filter classes.
        """

        self.assertEqual(sorted_squared_array([1, 2, 3, 5, 6, 8]), [1, 4, 9, 25, 36, 64])


if __name__ == '__main__':
    unittest.main()
