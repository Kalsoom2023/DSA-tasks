from funcs import RandomArray
from Insertion import InsertionSort
def HybridMerge(array, p, q, r):
    # left mid right
    n1 = q - p + 1
    n2 = r - q

    left_subarray = [0] * n1
    right_subarray = [0] * n2

    for i in range(n1):
        left_subarray[i] = array[p + i]

    for j in range(n2):
        right_subarray[j] = array[q + 1 + j]

    i = 0
    j = 0
    k = p

    while i < n1 and j < n2:
        if left_subarray[i] <= right_subarray[j]:
            array[k] = left_subarray[i]
            i += 1
        else:
            array[k] = right_subarray[j]
            j += 1
        k += 1

    while i < n1:
        array[k] = left_subarray[i]
        i += 1
        k += 1

    while j < n2:
        array[k] = right_subarray[j]
        j += 1
        k += 1

def HybridMergeSort(array, start, end):
     
    n = 32 
    if end - start <= n:
        InsertionSort(array, start, end)
    else:
        mid = (start + end) // 2
        HybridMergeSort(array, start, mid)
        HybridMergeSort(array, mid + 1, end)
        HybridMerge(array, start, mid, end)
    return array

import time

start_time = time.time()
start = 0
array = RandomArray(30)
end = 29

ans = HybridMergeSort(array, start, end)
end_time = time.time()
runtime = end_time - start_time
print("Runtime of program is", runtime, "seconds")

f = open(file=" SortedHybridMergeSort.csv", mode="w")
for i in ans:
    i = str(i)
    f.write(i + "\n")