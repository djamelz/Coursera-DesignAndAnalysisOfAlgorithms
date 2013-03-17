__author__ = 'Djamel'


class CustomHeap():

    def get(self):
        if len(self.heap_array) <= 0:
            return None
        return self.heap_array[0]

    def count(self):
        return len(self.heap_array)