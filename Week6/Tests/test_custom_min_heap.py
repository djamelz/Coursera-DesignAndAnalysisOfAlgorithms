__author__ = 'Djamel'

import unittest
import custom_min_heap as ch


class TestCustomMinHeap(unittest.TestCase):

    def test_insert_one_element_empty_heap(self):
        heap = ch.CustomMinHeap()
        heap.insert(1)
        self.assertEqual([1], heap.heap_array)

    def test_insert_several_elements(self):
        heap = ch.CustomMinHeap()
        heap.insert(4)
        heap.insert(4)
        heap.insert(8)
        heap.insert(9)
        heap.insert(4)
        heap.insert(12)
        heap.insert(9)
        heap.insert(11)
        heap.insert(13)

        heap.insert(7)
        heap.insert(20)
        heap.insert(5)

        self.assertEqual([4,
                          4, 5,
                          9, 4, 8, 9,
                          11, 13, 7, 20, 12], heap.heap_array)

    def test_pop_min_several_elements(self):
        heap = ch.CustomMinHeap()
        heap.heap_array = [4,
                           4, 8,
                           9, 4, 12, 9,
                           11, 13]

        current = heap.pop_min()

        self.assertEqual(current, 4)
        self.assertEqual([4,
                          4, 8,
                          9, 13, 12, 9,
                          11], heap.heap_array)

    def test_pop_min_3_elements(self):
        heap = ch.CustomMinHeap()
        heap.heap_array = [4,
                           4, 5]

        current = heap.pop_min()

        self.assertEqual(current, 4)
        self.assertEqual([4,
                          5], heap.heap_array)

    def test_pop_min_1_element(self):
        heap = ch.CustomMinHeap()
        heap.heap_array = [4]

        current = heap.pop_min()

        self.assertEqual(current, 4)
        self.assertEqual([], heap.heap_array)

    def test_pop_min_no_element(self):
        heap = ch.CustomMinHeap()

        current = heap.pop_min()

        self.assertEqual(current, None)
        self.assertEqual([], heap.heap_array)

    def test_pop_min_2_elements(self):
        heap = ch.CustomMinHeap()
        heap.heap_array = [4,
                           5]

        current = heap.pop_min()

        self.assertEqual(current, 4)
        self.assertEqual([5], heap.heap_array)

    def test_insert(self):
        heap = ch.CustomMinHeap()
        heap.insert(100)
        heap.insert(60)
        self.assertEqual([60, 100], heap.heap_array)
        heap.insert(50)
        self.assertEqual([50, 100, 60], heap.heap_array)
        heap.insert(90)
        self.assertEqual([50, 90, 60, 100], heap.heap_array)
