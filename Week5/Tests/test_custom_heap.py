__author__ = 'Djamel'

import unittest
import custom_heap as ch


class TestCustomHeap(unittest.TestCase):

    def test_insert_one_element_empty_heap(self):
        heap = ch.CustomHeap()
        heap.insert((1, "toto"))
        self.assertEqual([(1, "toto")], heap.heap_array)

    def test_insert_several_elements(self):
        heap = ch.CustomHeap()
        heap.insert((4, "4"))
        heap.insert((4, "4"))
        heap.insert((8, "8"))
        heap.insert((9, "9"))
        heap.insert((4, "4"))
        heap.insert((12, "12"))
        heap.insert((9, "9"))
        heap.insert((11, "11"))
        heap.insert((13, "13"))

        heap.insert((7, "7"))
        heap.insert((20, "20"))
        heap.insert((5, "5"))

        self.assertEqual([(4, "4"),
                          (4, "4"), (5, "5"),
                          (9, "9"), (4, "4"), (8, "8"), (9, "9"),
                          (11, "11"), (13, "13"), (7, "7"), (20, "20"), (12, "12")], heap.heap_array)

    def test_pop_min_several_elements(self):
        heap = ch.CustomHeap()
        heap.heap_array = [(4, "4"),
                           (4, "4"), (8, "8"),
                           (9, "9"), (4, "4"), (12, "12"), (9, "9"),
                           (11, "11"), (13, "13")]

        current = heap.pop_min()

        self.assertEqual(current, (4, "4"))
        self.assertEqual([(4, "4"),
                          (4, "4"), (8, "8"),
                          (9, "9"), (13, "13"), (12, "12"), (9, "9"),
                          (11, "11")], heap.heap_array)

    def test_pop_min_3_elements(self):
        heap = ch.CustomHeap()
        heap.heap_array = [(4, "4"),
                           (4, "4"), (5, "5")]

        current = heap.pop_min()

        self.assertEqual(current, (4, "4"))
        self.assertEqual([(4, "4"),
                          (5, "5")], heap.heap_array)

    def test_pop_min_1_element(self):
        heap = ch.CustomHeap()
        heap.heap_array = [(4, "4")]

        current = heap.pop_min()

        self.assertEqual(current, (4, "4"))
        self.assertEqual([], heap.heap_array)

    def test_pop_min_no_element(self):
        heap = ch.CustomHeap()

        current = heap.pop_min()

        self.assertEqual(current, None)
        self.assertEqual([], heap.heap_array)

    def test_pop_min_2_elements(self):
        heap = ch.CustomHeap()
        heap.heap_array = [(4, "4"),
                           (5, "5")]

        current = heap.pop_min()

        self.assertEqual(current, (4, "4"))
        self.assertEqual([(5, "5")], heap.heap_array)

    def test_insert(self):
        heap = ch.CustomHeap()
        heap.insert((100, "100"))
        heap.insert((60, "60"))
        self.assertEqual([(60, "60"), (100, "100")], heap.heap_array)
        heap.insert((50, "50"))
        self.assertEqual([(50, "50"), (100, "100"), (60, "60")], heap.heap_array)
        heap.insert((90, "90"))
        self.assertEqual([(50, "50"), (90, "90"), (60, "60"), (100, "100")], heap.heap_array)
