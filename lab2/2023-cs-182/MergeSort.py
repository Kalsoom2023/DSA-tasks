from funcs import RandomArray
def Merge(array, p, q, r):
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

def MergeSort(array, start, end):
    # left right
    if start < end:
        mid = (start + end) // 2
        MergeSort(array, start, mid)
        MergeSort(array, mid + 1, end)
        Merge(array, start, mid, end)
    return array

import time

start_time = time.time()
start = 0
array = RandomArray(30000)
end = 29999

ans = MergeSort(array, start, end)
end_time = time.time()
runtime = end_time - start_time
print("Runtime of program is", runtime, "seconds")

f = open(file="SortedMergeSort.csv", mode="w")
for i in ans:
    i = str(i)
    f.write(i + "\n")