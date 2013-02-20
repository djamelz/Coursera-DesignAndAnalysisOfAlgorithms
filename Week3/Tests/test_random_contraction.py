__author__ = 'Djamel'

import unittest
import random_contraction as rc


class TestRandomContraction(unittest.TestCase):

    def test_build_graph(self):
        vertices, edges = rc.build_graph("//projects/Coursera-DesignAndAnalysisOfAlgorithms/week3/test.txt")
        self.assertEqual(vertices, ["1", "2", "3", "4"])
        self.assertEqual(edges[0], ("1", "2"))
        self.assertEqual(edges[1], ("1", "4"))
        self.assertEqual(edges[2], ("2", "1"))
        self.assertEqual(edges[3], ("2", "3"))
        self.assertEqual(edges[4], ("2", "4"))
        self.assertEqual(edges[5], ("3", "2"))
        self.assertEqual(edges[6], ("4", "1"))
        self.assertEqual(edges[7], ("4", "2"))

    def test_compute_with_graph_4_vertices(self):
        self.assertEqual(rc.compute("//projects/Coursera-DesignAndAnalysisOfAlgorithms/week3/test.txt"), 1)

    def test_compute_with_test2(self):
        self.assertEqual(rc.compute("//projects/Coursera-DesignAndAnalysisOfAlgorithms/week3/test2.txt"), 4)

    def test_compute_week3(self):
        self.assertEqual(rc.compute("//projects/Coursera-DesignAndAnalysisOfAlgorithms/week3/kargerMinCut.txt", 100), 17)
