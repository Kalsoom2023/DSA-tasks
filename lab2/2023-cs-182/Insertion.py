from funcs import RandomArray
def InsertionSort(array,start, end):

 array=array[start:end+1]
 n=len(array)
 for i in range(1, n):
        key = array[i]
        j = i - 1
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key
 
 return array

import time
start_time = time.time()
start=0
array=RandomArray(1000)
end=999
ans= InsertionSort(array,start,end)
end_time = time.time()
runtime = end_time - start_time
print("Runtime of program at is for Insertion",runtime,"seconds")
f = open (file="SortedInsertionsort.csv", mode="w")
for i in ans:
 i=str(i)
 f.write (i+"\n")