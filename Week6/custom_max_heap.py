__author__ = 'Djamel'

import custom_heap


class CustomMaxHeap(custom_heap.CustomHeap):

    def __init__(self):
        self.heap_array = []

    def insert(self, item):
        self.heap_array.append(item)
        index = len(self.heap_array)
        if index == 1:
            return

        parent_index = int(index / 2)
        value = item

        while value > self.heap_array[parent_index - 1]:
            self.heap_array[index - 1], self.heap_array[parent_index - 1] = \
                self.heap_array[parent_index - 1], self.heap_array[index - 1]
            index = parent_index
            if index == 1:
                break
            else:
                parent_index = int(index / 2)

    def pop_max(self):
        if len(self.heap_array) <= 0:
            return None

        returned = self.heap_array[0]
        self.heap_array[0] = self.heap_array[-1]
        del (self.heap_array[-1])
        array_size = len(self.heap_array)

        if array_size <= 1:
            return returned

        value = self.heap_array[0]
        index = 1
        child_index = 2 * index
        if child_index + 1 <= array_size and self.heap_array[child_index - 1] < self.heap_array[child_index]:
            child_index += 1

        while value < self.heap_array[child_index - 1]:
            self.heap_array[index - 1], self.heap_array[child_index - 1] = \
                self.heap_array[child_index - 1], self.heap_array[index - 1]
            index = child_index
            child_index = 2 * index
            if child_index > array_size:
                break
            if child_index + 1 <= array_size and self.heap_array[child_index - 1] < self.heap_array[child_index]:
                child_index += 1
        return returned