__author__ = 'Djamel'


counter = 0

def compute(file):
    global counter
    counter = 0
    numbers = []
    with open(file) as f:
        for line in f:
            numbers.append(int(line))
    return count(numbers)

def count(A):
    n = len(A)
    if n==1:
        return A
    nn = int(round(n/2))
    left = count(A[0:nn])
    right = count(A[nn:n])
    return merge_and_count_split_inv(left,right)


def merge_and_count_split_inv(left,right):
    global counter
    merged = []
    i=0
    i_end = False
    j=0
    j_end = False
    for k in range(0,len(left)+len(right)):
       if i_end == False and (j_end or left[i] <= right[j]):
           merged.append(left[i])
           if i == len(left) - 1:
               i_end = True
           else:
               i += 1
       else:
           merged.append(right[j])
           if j == len(right) - 1:
               j_end = True
           else:
               j += 1
           if i_end == False:
               counter += len(left) - i
    return merged


def brute_force(file):
    numbers = []
    with open(file) as f:
        for line in f:
            numbers.append(int(line))
    count = 0
    for i in range(0,len(numbers)-1):
        for j in range(i+1,len(numbers)):
            if numbers[i]>numbers[j]:
                count+=1
    return count





def sort_and_count(A, n):
    if n==1:
        return 0
