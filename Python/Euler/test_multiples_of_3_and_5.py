import unittest
from multiples_of_3_and_5 import sum_multiples


class TestSumMultiples(unittest.TestCase):
    """Tests for the 'multiples_of_3_and_5.py'."""

    def test_range(self):
        """Tests for values passed in range max and multiples"""

        # Test sum when range max >= 0
        self.assertEqual(sum_multiples(0, [3, 5]), 0)
        self.assertEqual(sum_multiples(1, [1]), 0)
        self.assertEqual(
            sum_multiples(10.1, [3, 5]),
            sum({i for i in range(1, 10) if i % 3 == 0} |
                {i for i in range(1, 10) if i % 5 == 0}))
        self.assertEqual(
            sum_multiples(10, [-3, -5]),
            sum({i for i in range(1, 10) if i % 3 == 0} |
                {i for i in range(1, 10) if i % 5 == 0}))

    def test_values(self):
        """Make sure value errors are raised when necessary"""

        with self.assertRaises(ValueError):
            sum_multiples(-20, [3, 5])

    def test_type(self):
        """Make sure type errors are raised when necessary"""

        with self.assertRaises(TypeError):
            sum_multiples(3 + 5j, [3, 5])
            sum_multiples(True, [3, 5])
            sum_multiples("maximum", [3, 5])
            sum_multiples(10, [3 + 5j])
            sum_multiples(10, [3 + 5j])
            sum_multiples(10, 0.5)
            sum_multiples(10, True)
            sum_multiple(10, "maximum")


if __name__ == "__main__":
    unittest.main()
