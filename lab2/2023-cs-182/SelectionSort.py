
from funcs import RandomArray
def SelectionSort(array,start, end):

 array=array[start:end]
 n=len(array)
 for i in range(n-1):
    min_idx = i
    for j in range(i+1, n):
        if array[min_idx] > array[j]:
            min_idx = j
            
      
    array[i], array[min_idx] = array[min_idx], array[i]
  
 return array
     
import time
start_time = time.time()
start=0
end=10
array=RandomArray(11)
ans= SelectionSort(array,start,end)
end_time = time.time()
runtime = end_time - start_time
print("Runtime of program at is",runtime,"seconds")
f = open (file="SortedSelectionsort.csv", mode="w")
for i in ans:
 i=str(i)
 f.write (i+"\n")