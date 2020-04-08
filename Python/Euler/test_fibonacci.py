import unittest
from fibonacci import fibonacci


class TestFibonacci(unittest.TestCase):
    "Tests for 'fibonacci.py'"

    def test_fibo(self):
        """Tests results for different input values"""
        self.assertEqual(fibonacci(2), [0, 1, 1, 2])

    def test_values(self):
        """Make sure all value errors are raised when necessary"""
        with self.assertRaises(ValueError):
            fibonacci(-10)
            fibonacci(10, 11)
            fibonacci(10, -1)

    def test_type(self):
        """Make sure all type errors are raised when necessary"""
        with self.assertRaises(TypeError):
            fibonacci(True)
            fibonacci(3 + 5j)
            fibonacci("string")
            fibonacci(False)
            fibonacci(88.5)
            fibonacci(10, 'me')
            fibonacci(10, 3 + 5j)
            fibonacci(10, 4.5)


if __name__ == "__main__":
    unittest.main()
