import unittest

from .app import fibonacci


class TestSum(unittest.TestCase):
    def test_fibonacci(self):
        self.assertEqual(fibonacci(1), 1)
        self.assertEqual(fibonacci(2), 1)
        self.assertEqual(fibonacci(3), 2)
        self.assertEqual(fibonacci(4), 3)
        self.assertEqual(fibonacci(5), 5)
        self.assertEqual(fibonacci(6), 8)
        self.assertEqual(fibonacci(7), 13)

    def test_fibonacci_negative(self):
        self.assertEqual(fibonacci(-1), None)

    def test_fibonacci_string(self):
        self.assertEqual(fibonacci("a"), None)

    def test_fibonacci_float(self):
        self.assertEqual(fibonacci(1.0), None)


if __name__ == "__main__":
    unittest.main()
