__author__ = 'Djamel'


def compute(file, exercice_number):
    numbers = []
    with open(file) as f:
        for line in f:
            numbers.append(int(line))
    print numbers
    sorted_numbers, counter = partition(numbers, 0, 0, len(numbers), exercice_number)
    print sorted_numbers
    return counter


def partition(numbers, counter, start, end, pivot_index_type):
    if end - start <= 1: return numbers, counter
    #print numbers[start:end]
    counter = counter + end - start - 1

    i = start
    pivot_index = start
    if pivot_index_type == 2: numbers[start], numbers[end-1] = numbers[end-1], numbers[start]
    if pivot_index_type == 3:
        median = get_median(numbers[start:end]) + start
        numbers[start], numbers[median] = numbers[median], numbers[start]
    pivot = numbers[pivot_index]

    for j in range(start, end):
        if numbers[j] < pivot:
            i += 1
            numbers[i], numbers[j] = numbers[j], numbers[i]

    numbers[pivot_index], numbers[i] = numbers[i], numbers[pivot_index]
    numbers, counter = partition(numbers, counter, start, i, pivot_index_type)
    numbers, counter = partition(numbers, counter, i + 1, end, pivot_index_type)

    return numbers, counter

def get_median(numbers):
    size = len(numbers)
    middle = int(size / 2 + size % 2) - 1

    x = numbers[0]
    y = numbers[middle]
    z = numbers[size - 1]

    if x > y:
        if z < y: return middle
        elif x < z: return 0
        else: return size - 1
    elif z > y: return middle
    elif x < z: return size - 1
    else: return 0



