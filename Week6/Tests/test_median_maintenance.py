__author__ = 'Djamel'


import unittest
import median_maintenance as mm


class TestMedianMaintenance(unittest.TestCase):

    def test_compute_median_maintenance_test1(self):
        self.assertEqual(50, mm.compute_median_maintenance("//projects/Coursera-DesignAndAnalysisOfAlgorithms/week6/MedianTest1.txt"))

    def test_compute_median_maintenance_test2(self):
        self.assertEqual(8046, mm.compute_median_maintenance("//projects/Coursera-DesignAndAnalysisOfAlgorithms/week6/MedianTest2.txt"))


    def test_compute_median_maintenance(self):
        self.assertEqual(1213, mm.compute_median_maintenance("//projects/Coursera-DesignAndAnalysisOfAlgorithms/week6/Median.txt"))