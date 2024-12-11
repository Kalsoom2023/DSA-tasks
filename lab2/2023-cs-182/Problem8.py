from funcs import RandomArray,ShuffleArray
import time
def MergeForWords(array, p, q, r):
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
        if len(left_subarray[i]) <= len(right_subarray[j]):
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

def MergeSortForWords(array, start, end):
    # left right
    if start < end:
        mid = (start + end) // 2
        MergeSortForWords(array, start, mid)
        MergeSortForWords(array, mid + 1, end)
        MergeForWords(array, start, mid, end)
    return array
def InsertionSortForWords (words,n):
  for i in range(1, n):
        key = words[i]
        j = i - 1
        while j >= 0 and len(key) < len(words[j]):
            words[j + 1] = words[j]
            j -= 1
        words[j + 1] = key

  return words
given_file = open (file = 'words.txt', mode = 'r')
lines = given_file. read ()
words = []
arr = lines.split()
for s in arr:
 word = str(s)
 words.append(word)

n=len(words)
start_time = time.time()
InsertionSortForWords(words,n)
end_time = time.time()
runtime = end_time - start_time
print("Runtime for insertion:",runtime)
start_time = time.time()
MergeSortForWords(words,0,len(words)-1)
end_time = time.time()
runtime = end_time - start_time
print("Runtime for merge:",runtime)
ShuffleArray(words,0,len(words)-1)
start_time = time.time()
InsertionSortForWords(words,n)
end_time = time.time()
runtime = end_time - start_time
print("Runtime for insertion:",runtime)
start_time = time.time()
MergeSortForWords(words,0,len(words)-1)
end_time = time.time()
runtime = end_time - start_time
print("Runtime for merge:",runtime)