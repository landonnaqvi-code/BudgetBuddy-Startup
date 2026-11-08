import unittest
import sys
from features.reports import *

class TestAverageBalance(unittest.TestCase):
    def test_empty_history(self):
        self.assertEqual(average_balance({"history": []}), 0.0)
    def test_average_calculated_correctly(self):
        self.assertEqual(average_balance({"history": [5, 6, 4]}), 5.0)