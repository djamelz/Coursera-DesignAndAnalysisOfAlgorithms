__author__ = 'Djamel'



import unittest
import custom_max_heap as ch


class TestCustomMaxHeap(unittest.TestCase):

    def test_insert_one_element_empty_heap(self):
        heap = ch.CustomMaxHeap()
        heap.insert((1, "toto"))
        self.assertEqual([(1, "toto")], heap.heap_array)

    def test_insert_several_elements(self):
        heap = ch.CustomMaxHeap()
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

        self.assertEqual([20,
                          13, 9,
                          11, 12, 5, 9,
                          4, 8, 4, 7, 4], heap.heap_array)

    def test_pop_max_several_elements(self):
        heap = ch.CustomMaxHeap()
        heap.heap_array = [20,
                           13, 9,
                           11, 12, 5, 9,
                           4, 8, 4, 7, 4]

        current = heap.pop_max()

        self.assertEqual(current, 20)
        self.assertEqual([13,
                          12, 9,
                          11, 7, 5, 9,
                          4, 8, 4, 4], heap.heap_array)

    def test_pop_max_3_elements(self):
        heap = ch.CustomMaxHeap()
        heap.heap_array = [6,
                           4, 5]

        current = heap.pop_max()

        self.assertEqual(current, 6)
        self.assertEqual([5,
                          4], heap.heap_array)

    def test_pop_max_1_element(self):
        heap = ch.CustomMaxHeap()
        heap.heap_array = [4]

        current = heap.pop_max()

        self.assertEqual(current, 4)
        self.assertEqual([], heap.heap_array)

    def test_pop_max_no_element(self):
        heap = ch.CustomMaxHeap()

        current = heap.pop_max()

        self.assertEqual(current, None)
        self.assertEqual([], heap.heap_array)

    def test_pop_max_2_elements(self):
        heap = ch.CustomMaxHeap()
        heap.heap_array = [5,
                           4]

        current = heap.pop_max()

        self.assertEqual(current, 5)
        self.assertEqual([4], heap.heap_array)

    def test_insert(self):
        heap = ch.CustomMaxHeap()
        heap.insert(100)
        heap.insert(60)
        self.assertEqual([100, 60], heap.heap_array)
        heap.insert(50)
        self.assertEqual([100, 60, 50], heap.heap_array)
        heap.insert(90)
        self.assertEqual([ 100, 90, 50, 60], heap.heap_array)
