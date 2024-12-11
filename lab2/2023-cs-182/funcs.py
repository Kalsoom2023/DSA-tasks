def RandomArray(size):
  import random
  array = []
  min = 0
  max = 100
  for i in range (0, size):
    num = random. randint (min, max)
    array. append (num)
  return array

def ShuffleArray(array,start,end):
 import random
 n=end
 for i in range(n):
    random_index = random.randint(0, n)
    temp = array.pop(random_index)
    array.append(temp)
 return array