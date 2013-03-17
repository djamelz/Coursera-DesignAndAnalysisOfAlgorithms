__author__ = 'Djamel'

import custom_min_heap as min_h
import custom_max_heap as max_h


def compute_median_maintenance(file):
    hh = min_h.CustomMinHeap()
    hl = max_h.CustomMaxHeap()

    median_sum = 0

    with open(file) as f:
        for line in f:
            number = int(line.rstrip("\n").rstrip("\r").rstrip("\t"))
            #print median_sum

            if hl.count() == 0 and hh.count() == 0:
                hl.insert(number)
                median_sum += number
                continue

            if hl.get() >= number:
                hl.insert(number)
            else:
                hh.insert(number)

            balance = hl.count() - hh.count()

            if balance == 0 or balance == 1:
                median_sum += hl.get()
            elif balance == 2:
                hh.insert(hl.pop_max())
                median_sum += hl.get()
            elif balance == -1:
                median_sum += hh.get()
            elif balance == -2:
                hl.insert(hh.pop_min())
                median_sum += hl.get()
    return median_sum % 10000


