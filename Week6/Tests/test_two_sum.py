__author__ = 'Djamel'

import unittest
import two_sum as ts

class TestTwoSum(unittest.TestCase):

    def test_compute_two_sum_with_twosummedium_file_interval_30_60(self):
        self.assertEqual(9, ts.compute_two_sum("//projects/Coursera-DesignAndAnalysisOfAlgorithms/week6/twosummedium.txt",30,60))

    def test_compute_two_sum_with_twosummedium_file_interval_60_100(self):
        self.assertEqual(28, ts.compute_two_sum("//projects/Coursera-DesignAndAnalysisOfAlgorithms/week6/twosummedium.txt",60,100))

    def test_compute_two_sum(self):
        self.assertEqual(1477, ts.compute_two_sum("//projects/Coursera-DesignAndAnalysisOfAlgorithms/week6/HashInt.txt",2500,4000))