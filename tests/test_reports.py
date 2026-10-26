import unittest
import sys
from features.reports import *

class TestAverageBalance(unittest.TestCase):
    def test_empty_history(self):
        self.assertEqual(average_balance({"history": []}), 0.0)