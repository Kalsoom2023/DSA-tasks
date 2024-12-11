from funcs import RandomArray
def BubbleSort(array,start, end):

 array=array[start:end+1]
 
 n = len(array)
 for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
                swapped = True
        if (swapped == False):
            break
 
 return array

import time
start_time = time.time()
start=0
end=10
array=RandomArray(11)
ans= BubbleSort(array,start,end)
end_time = time.time()
runtime = end_time - start_time
print("Runtime of program at is",runtime,"seconds")
f = open (file="SortedBubblesort.csv", mode="w")
for i in ans:
 i=str(i)
 f.write (i+"\n")