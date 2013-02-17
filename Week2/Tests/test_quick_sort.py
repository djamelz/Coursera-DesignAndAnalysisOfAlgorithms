__author__ = 'Djamel'


import unittest
import quick_sort as qs


class TestQuickSort(unittest.TestCase):

    def test_compute_with_test_first_pivot(self):
        self.assertEqual(qs.compute("//projects/Coursera-DesignAndAnalysisOfAlgorithms/week2/test.txt", 1), 45)

    def test_compute_with_test2_first_pivot(self):
        self.assertEqual(qs.compute("//projects/Coursera-DesignAndAnalysisOfAlgorithms/week2/test2.txt", 1), 96)

    def test_compute_with_week1_first_pivot(self):
        self.assertEqual(qs.compute("//projects/Coursera-DesignAndAnalysisOfAlgorithms/week1/IntegerArray.txt", 1),
                         1954287)
    def test_compute_with_week2_first_pivot(self):
        self.assertEqual(qs.compute("//projects/Coursera-DesignAndAnalysisOfAlgorithms/week2/QuickSort.txt", 1),
                         162085)

    def test_compute_with_test_final_pivot(self):
        self.assertEqual(qs.compute("//projects/Coursera-DesignAndAnalysisOfAlgorithms/week2/test.txt", 2), 37)

    def test_compute_with_test2_final_pivot(self):
        self.assertEqual(qs.compute("//projects/Coursera-DesignAndAnalysisOfAlgorithms/week2/test2.txt", 2), 109)

    def test_compute_with_week1_final_pivot(self):
        self.assertEqual(qs.compute("//projects/Coursera-DesignAndAnalysisOfAlgorithms/week1/IntegerArray.txt", 2),
                         2047196)

    def test_compute_with_week2_final_pivot(self):
        self.assertEqual(qs.compute("//projects/Coursera-DesignAndAnalysisOfAlgorithms/week2/QuickSort.txt", 2),
                         164123)

    def test_compute_with_test_median_pivot(self):
        self.assertEqual(qs.compute("//projects/Coursera-DesignAndAnalysisOfAlgorithms/week2/test.txt", 3), 25)

    def test_compute_with_test2_median_pivot(self):
        self.assertEqual(qs.compute("//projects/Coursera-DesignAndAnalysisOfAlgorithms/week2/test2.txt", 3), 82)

    def test_compute_with_week1_median_pivot(self):
        self.assertEqual(qs.compute("//projects/Coursera-DesignAndAnalysisOfAlgorithms/week1/IntegerArray.txt", 3),
                         1697653)

    def test_compute_with_week2_median_pivot(self):
        self.assertEqual(qs.compute("//projects/Coursera-DesignAndAnalysisOfAlgorithms/week2/QuickSort.txt", 3),
                         138382)

    def test_get_median_even_number(self):
        numbers = [1, 2, 3]
        self.assertEqual(qs.get_median(numbers), 1)

    def test_get_median_odd_number(self):
        numbers = [1, 2, 3, 4]
        self.assertEqual(qs.get_median(numbers), 1)

    def test_get_median_first_match(self):
        numbers = [38, 45, 1, 11]
        self.assertEqual(qs.get_median(numbers), 0)

    def test_get_median_last_match(self):
        numbers = [2000, 45, 38, 1, 652]
        self.assertEqual(qs.get_median(numbers), 4)