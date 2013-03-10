__author__ = 'Djamel'


import unittest
import shortest_path as sp


class TestShortestPath(unittest.TestCase):

    def test_shortest_path_test1(self):
        result = sp.compute("//projects/Coursera-DesignAndAnalysisOfAlgorithms/week5/DjikstraTest1.txt")
        self.assertEqual("0,10,50,30,60", result)

    def test_shortest_path_test2(self):
        result = sp.compute("//projects/Coursera-DesignAndAnalysisOfAlgorithms/week5/DjikstraTest2.txt")
        self.assertEqual("0,7,9,20,20,11", result)

    def test_shortest_path_test3(self):
        result = sp.compute("//projects/Coursera-DesignAndAnalysisOfAlgorithms/week5/DjikstraTest3.txt")
        self.assertEqual("0,1,3,1000000,1000000", result)


    def test_shortest_path(self):
        result = sp.compute("//projects/Coursera-DesignAndAnalysisOfAlgorithms/week5/dijkstraData.txt", True)
        self.assertEqual("2599,2610,2947,2052,2367,2399,2029,2442,2505,3068", result)