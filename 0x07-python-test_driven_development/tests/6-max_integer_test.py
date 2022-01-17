#!/usr/bin/python3
"""
Unit test for max_integer
"""


import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """
    Unit test class for max int
    """

    def test_module_docstring(self):
        """Test for module doc string"""
        modstring = __import__('6-max_integer').__doc__
        self.assertTrue(len(modstring) > 1)

    def test_function_docstring(self):
        """Test for function doc string"""
        funcstring = max_integer.__doc__
        self.assertTrue(len(funcstring) > 1)

    def test_empty(self):
        """Test if empty list"""
        self.assertEqual(max_integer([]), None)

    def test_negatives(self):
        """Check negative numbers"""
        self.assertEqual(max_integer([-1, -2, -3]), -1)

    def test_type(self):
        """Make sure input is a list"""
        self.assertIs(list, list)

    def test_invalid(self):
        self.assertRaises(TypeError, max_integer, [6, "hi mom", 7],
                          msg="unorderable types: str() > int()")
        self.assertRaises(TypeError, max_integer, [4, 0, "7"],
                          msg="unorderable types: str() > int()")

if __name__ == "__main__":
    unittest.main()
