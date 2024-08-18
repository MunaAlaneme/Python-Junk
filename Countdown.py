# July 16, 2024
import unittest
from countdown import countdown

class TestCountdown(unittest.TestCase):

    def test_countdown_positive_number(self):
        self.assertEqual(countdown(5), [5, 4, 3, 2, 1, 0])

    def test_countdown_zero(self):
        self.assertEqual(countdown(0), [0])

    def test_countdown_negative_number(self):
        self.assertEqual(countdown(-3), [-3, -2, -1, 0])

    def test_countdown_large_number(self):
        self.assertEqual(countdown(100), list(range(100, -1, -1)))

    def test_countdown_float_number(self):
        self.assertEqual(countdown(3.5), [3.5, 2.5, 1.5, 0.5, -0.5])

if __name__ == '__main__':
    unittest.main()