__author__ = 'Djamel'


def compute_two_sum(file, from_number, to_number):
    numbers = dict()
    counter = 0

    with open(file) as f:
        for line in f:
            number = int(line.rstrip("\n").rstrip("\r").rstrip("\t"))
            if number <= to_number:
                if number in numbers:
                    numbers[number] = 2
                else:
                    numbers[number] = 1

    for interval in xrange(from_number, to_number + 1):
        for number in numbers.keys():
            substract = (interval - number)
            if substract in numbers.keys():
                if number == (interval / 2) and numbers[number] <= 1:
                    continue
                counter += 1
                #print number, "+", substract, "=", interval
                break

    return counter