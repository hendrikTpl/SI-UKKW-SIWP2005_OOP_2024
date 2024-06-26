import unittest
from calculator.basic_operations import add, subtract, multiply, divide

class TestBasicOperations(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(1, 2), 3)
        self.assertEqual(add(-1, 1), 0)

    def test_subtract(self):
        self.assertEqual(subtract(2, 1), 1)
        self.assertEqual(subtract(2, 2), 0)

    def test_multiply(self):
        self.assertEqual(multiply(3, 2), 6)
        self.assertEqual(multiply(-3, 2), -6)

    def test_divide(self):
        self.assertEqual(divide(4, 2), 2)
        with self.assertRaises(ValueError):
            divide(1, 0)

unittest.main()
