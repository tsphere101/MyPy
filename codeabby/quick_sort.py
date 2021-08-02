import random
from time import time


def quicksort(data):

    if len(data) <= 1:
        return data

    pivot_pos = random.randint(0,len(data)-1)
    pivot = data[pivot_pos]

    data.pop(pivot_pos)

    lower = []
    upper = []

    for i in range(len(data)):
        if data[i] <= pivot:
            lower.append(data[i])

        else:
            upper.append(data[i])

    result = []
    for d in quicksort(lower):
        result.append(d)

    result.append(pivot)

    for d in quicksort(upper):
        result.append(d)

    return result


def quicksort_new(data):
    if len(data) <= 1:
        return data

    lower, equals, upper = [], [], []

    pivot = data[random.randint(0, len(data)-1)]

    for d in data:
        if d == pivot: equals.append(d)
        elif d > pivot: upper.append(d)
        elif d < pivot: lower.append(d)

    return quicksort(lower) + equals + quicksort(upper)

def create_random_list(length = 10,max = 50) :
    result = []
    for _ in range(length) :
        result.append(random.randint(0,max))
    return result

if __name__ == "__main__":

    a = create_random_list(10000)
    tot_time1 = 0.0
    tot_time2 = 0.0
    

    t0 = time()
    s = quicksort(a)
    t1 = time()

    t2 = time()
    s = quicksort_new(a)
    t3 = time()

    tot_time1 += t1-t0
    tot_time2 += t3-t2
    for x in s :
        print(x)
    print(tot_time1)
    print(tot_time2)