def SearchA(Arr, x):
    indices= []
    for p in range(len(arr)):
      if(x==arr[p]):
        indices.append(p)
    return indices

arr=[22,2,1,7,11,13,5,2,9]
x = int(input("Enter the number:"))
print("Index:",SearchA(arr,x))
#Problem2
def SearchB(Arr, x):
    indices= []
    a=0
    for p in range(len(arr)):
      if(x!=arr[p]):
        a=a+1
      if (x==arr[p]):
        indices.append(a)
        a=a+1
    return indices

arr=[1,2,2,5,9,7,11,13,22]
x = int(input("Enter the number:"))
print("Index:",SearchB(arr,x))
#Problem3
def Minimum(Arr, starting, ending):
    
    minimumIndex=starting
    for p in range(starting+1,ending+1):
      if(Arr[p]<Arr[minimumIndex]):
        minimumIndex=p
     
    
    return minimumIndex

Array= []
n=int(input("Enter the size of array "))

for i in range(0,n):
    ele=int(input())
    Array.append(ele)

StartingIndex= int(input("StartingIndex"))
EndingIndex= int(input("EndingIndex"))
print(Minimum(Array,StartingIndex,EndingIndex))
#Problem4
def Sort4(Arr):
    sortarray=[]
    while Arr:
    
        minIndex = Minimum(Arr, 0, len(Arr) - 1)
        
        minValue=Arr[minIndex]
        sortarray.append(minValue)
        Arr.pop(minIndex)
       
    
    return sortarray

Array= [3,4,7,8,0,1,23,-2,-5]
print(Sort4(Array))
 
#Problem5
def stringReverse(s, starting, ending):
    extractedArray = s[starting:ending + 1]
    reversedArray = extractedArray[::-1]
    
    return reversedArray


s = "University of Engineering and Technology Lahore"
starting = 11
ending = 34
print(stringReverse(s, starting, ending)) 
#Problem6
def SumIterative(number):
    number = abs(number)
    total = 0
    while number > 0:
        total += number % 10  
        number =number// 10          
    
    return total
def SumRecursive(number):
    number=abs(number)
    if number == 0:
        return 0
    
    else:
        sum= number % 10 + SumRecursive(number // 10)
        return sum
a=int(input("Enter A number:"))
print(SumIterative(a))
print(SumRecursive(a))
#Problem7
def RowWiseSum(Mat):
    sums=[]
    sum=0
    num_cols=len(Mat[0])
    for i in range (num_cols):
            for j in range (len(Mat)):
                sum = sum + Mat[i][j] 
            sums.append(sum)
            sum = 0;
 
    return sums    

def ColumnWiseSum(Mat):
    sums=[]
    sum2=0
    num_cols=len(Mat[0])
    for i in range (num_cols):
            for j in range (len(Mat)):
                sum2 = sum2 + Mat[j][i] 
            sums.append(sum2)
            sum2 = 0;
 
    
    return sums  

A = [
    [1, 13, 13],
    [5, 11, 6],
    [4, 4, 9]
]


row_sums=[]
column_sums=[]
row_sums = RowWiseSum(A)
column_sums=ColumnWiseSum(A)

print("Row-wise:")
for sum in row_sums:
    print(sum) 
print("Column-wise:", end=" ")
print(" ".join(map(str, column_sums)))  

#Problem8
def SortedMerge(Arr1, Arr2):
    n=len(Arr1)
    m=len(Arr2)
    temp=0
    for i in range (len(Arr2)):
        Arr1.append(Arr2[i])
    for i in range (len(Arr1)):
         for  j in range (len(Arr1)-i-1):
            if (Arr1[j] > Arr1[j+1]):
                temp = Arr1[j]
                Arr1[j] = Arr1[j+1]
                Arr1[j+1] = temp
            
    return Arr1
    
Arr1 = [0,3,4,10,11]
Arr2 = [1,8,13,24]
print(SortedMerge(Arr1,Arr2))
#Problem9
def PalindromRecursive(str):
   if str==str[::-1]:
       return True
   else:
       return False
string=input("Word:")
if(PalindromRecursive(string)):
    print("Palindrome")
else:
    print("No")
#Problem10
def Sort10(Arr):
    Arr.sort()
    Arr2=[]
    Arr3=[]
    i=0
    for i in range(len(Arr)):
        if Arr[i]<0:
            Arr2.append(Arr[i])
        else:
            Arr3.append(Arr[i])
    sorted_array=[]
    max_len = max(len(Arr2), len(Arr3))
    for i in range(max_len):
      if i < len(Arr2):
        sorted_array.append(Arr2[i])
      if i < len(Arr3):
        sorted_array.append(Arr3[i])

    return sorted_array
Input= [10, -1, 9, 20, -3, -8, 22, 9, 7]
print(Sort10(Input))
    