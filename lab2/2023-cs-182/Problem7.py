from Insertion import InsertionSort
from SelectionSort import SelectionSort
from BubbleSort import BubbleSort
from HybridMerge import HybridMergeSort
from MergeSort import MergeSort
import time
from funcs import RandomArray
given_file = open (file = 'Nvalues.txt', mode = 'r')
lines = given_file. read ()
numbers = []
methods=['InsertionSort','MergeSort','HybridMergeSort','SelectionSort','BubbleSort']
arr = lines.split()
f = open(file="Runtime.csv", mode="w")
for s in arr:
 num = int(s)
 numbers.append(num)
 
for num in numbers:
  array=RandomArray(num)
  for method in methods:
      start_time = time.time()
      ans=globals()[method](array,0,num-1)
      end_time = time.time()
      runtime = end_time - start_time
      i = str(runtime)
      f.write(i + " ")
  f.write("\n")