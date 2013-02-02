__author__ = 'Djamel'



def compute(file):
    numbers = []
    with open(file) as f:
        for line in f:
            numbers.append(int(line))
    return count(numbers, counter = 0)[1]

def count(A, counter):
    n = len(A)
    if n==1: return (A,counter)
    nn = int(round(n/2))
    left = count(A[:nn],counter)
    right = count(A[nn:],left[1])
    return merge_and_count_split_inv(left[0],right[0],right[1])



def merge_and_count_split_inv(left,right, counter):
    merged = []
    i = 0
    j = 0
    i_end = False
    j_end = False
    for k in range(0,len(left)+len(right)):
       if i_end == False and (j_end or left[i] <= right[j]):
           merged.append(left[i])
           if i == len(left) - 1: i_end = True
           else: i += 1
       else:
           merged.append(right[j])
           if j == len(right) - 1: j_end = True
           else: j += 1
           if i_end == False:
               counter += len(left) - i
    return (merged, counter)


def brute_force(file):
    numbers = []
    with open(file) as f:
        for line in f:
            numbers.append(int(line))
    count = 0
    for i in range(0,len(numbers)-1):
        for j in range(i+1,len(numbers)):
            if numbers[i]>numbers[j]: count+=1
    return count





def sort_and_count(A, n):
    if n==1:
        return 0
