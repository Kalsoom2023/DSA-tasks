import numpy as np

def printMatrix(A, startingIndex, rows, columns):
    firstrow, firstcol = startingIndex
    for i in range(0, firstrow + rows):
        for j in range(0, firstcol + columns):
            print(A[i][j], end=' ')
        print()
A = [
    [3, 4, 5],
    [2, 5, 7]
]
printMatrix(A, (0, 0), 2, 3)
##
def MatAdd(A,B):
 result = [[0 for _ in range(len(A[0]))] for _ in range(len(A))]
 for i in range(len(A)):   
    for j in range(len(A[0])):
        result[i][j] = A[i][j] + B[i][j]
        

 return result
A = [[1,2,3],
    [1,2,3],
    [1,2,3]]
 
B = [[9,8,7],
    [6,2,5],
    [1,2,3]]
print(MatAdd(A,B))
##
def MatAddPartial(A, B, startingIndex, size):
    firstrow, firstcol = startingIndex
    result = [[0 for _ in range(len(A[0]))] for _ in range(len(A))]

    for i in range(len(A)):
        for j in range(len(A[0])):
            result[i][j] = A[i][j]
    for i in range(size):   
        for j in range(size):
            result[firstrow + i][firstcol + j] += B[firstrow + i][firstcol + j]

    return result

A = [
    [1, 2, 3],
    [1, 2, 3],
    [1, 2, 3]
]

B = [
    [9, 8, 7],
    [6, 2, 5],
    [1, 2, 3]
]
result = MatAddPartial(A, B, (1, 1), 2)
for row in result:
    print(row)
###
def MatMul(A, B):
    Arow = len(A)
    Acol = len(A[0])
    Bcol = len(B[0])
    
    result = [[0] * Bcol for _ in range(Arow)]
    
    for i in range(Arow):
        for j in range(Bcol):
            for k in range(Acol):
                result[i][j] += A[i][k] * B[k][j]
    
    return result
A = [
    [1, 2, 3],
    [1, 2, 3],
    [1, 2, 3]
]

B = [
    [9, 8, 7],
    [6, 2, 5],
    [1, 2, 3]
]
mat=(MatMul(A,B))
for rows in mat:
    print(rows)

###
def multiplyRecursive(A, B, result, i, j, k, row1, col1, col2):
    
    if i >= row1:
        return
    if j < col2:
        if k < col1:
            result[i][j] += A[i][k] * B[k][j]
            multiplyRecursive(A, B, result, i, j, k + 1, row1, col1, col2)
            return
        k = 0
        multiplyRecursive(A, B, result, i, j + 1, k, row1, col1, col2)
        return
    multiplyRecursive(A, B, result, i + 1, 0, 0, row1, col1, col2)

def MatMulRecursive(A, B):
    row1, col1 = len(A), len(A[0])
    row2, col2 = len(B), len(B[0])
    if col1 != row2:
        return
    result = []
    for _ in range(row1):
     row = []
     for _ in range(col2):
        row.append(0)
     result.append(row)
    multiplyRecursive(A, B, result, 0, 0, 0, row1, col1, col2)
    return result
    A = [
    [1, 2, 3],
    [1, 2, 3],
    [1, 2, 3]
]
B = [
    [1, 2, 3],
    [1, 2, 3],
    [1, 2, 3]
]

res=(MatMulRecursive(A, B))
for rows in res:
    print(rows)

###

import numpy as np

def strassen(A, B):
    a = A.shape[0]
    if a == 1:
        return A * B

    centre = a // 2
    A11, A12 = A[:centre, :centre], A[:centre, centre:]
    A21, A22 = A[centre:, :centre], A[centre:, centre:]
    B11, B12 = B[:centre, :centre], B[:centre, centre:]
    B21, B22 = B[centre:, :centre], B[centre:, centre:]

    p1 = strassen(A11 + A22, B11 + B22)
    p2 = strassen(A21 + A22, B11)
    p3 = strassen(A11, B12 - B22)
    p4 = strassen(A22, B21 - B11)
    p5 = strassen(A11 + A12, B22)
    p6 = strassen(A21 - A11, B11 + B12)
    p7 = strassen(A12 - A22, B21 + B22)

    c11 = p1 + p4 - p5 + p7
    c12 = p3 + p5
    c21 = p2 + p4

    c22 = p1 + p3 - p2 + p6

    c = np.vstack((np.hstack((c11, c12)), np.hstack((c21, c22))))

    return c
A = np.array([[1, 2, 3], [1, 2, 3]])
B = np.array([[2, 1], [2, 1], [1, 2]])

s = max(A.shape[0], A.shape[1], B.shape[0], B.shape[1])
n = 1
while n < s:
    n *= 2

A = np.pad(A, ((0, n - A.shape[0]), (0, n - A.shape[1])), mode='constant')
B = np.pad(B, ((0, n - B.shape[0]), (0, n - B.shape[1])), mode='constant')
c = strassen(A, B)
print(c[:A.shape[0], :B.shape[1]])
