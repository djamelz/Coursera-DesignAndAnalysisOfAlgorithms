__author__ = 'Djamel'

import unittest
import inversion_of_number as ion

class TestInversionOfNumber(unittest.TestCase):

    def test_compute(self):
        self.assertEqual(11,ion.compute("//projects/Coursera-DesignAndAnalysisOfAlgorithms/week1/IntegerArray-unittest.txt"))

    def test_brute_force(self):
        self.assertEqual(11,ion.brute_force("//projects/Coursera-DesignAndAnalysisOfAlgorithms/week1/IntegerArray-unittest.txt"))

    #def test_brute_force_full(self):
    #    self.assertEqual(2407905288,brute_force("//projects/Coursera-DesignAndAnalysisOfAlgorithms/week1/IntegerArray.txt"))

    def test_compute_full(self):
        self.assertEqual(2407905288,ion.compute("//projects/Coursera-DesignAndAnalysisOfAlgorithms/week1/IntegerArray.txt"))

    def test_compute_full2(self):
        self.assertEqual(2507223936,ion.compute("//projects/Coursera-DesignAndAnalysisOfAlgorithms/week1/IntegerArray-2.txt"))
