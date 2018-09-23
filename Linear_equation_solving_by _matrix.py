from numpy import *


def minor(a, i, j):
    ar = []
    if len(a)-1!= 2:
        for i1 in range(len(a)):
            for j1 in range(len(a[0])):
                if i1 != i and j1 != j:
                    ar.append(a[i1][j1])
                    
    for i1 in range(len(a)):
        for j1 in range(len(a[0])):
            if i1 != i and j1 != j:
                ar.append(a[i1][j1])
    return ((-1) ** (i + j)) * (a[i][j]) * (ar[0] * ar[3] - ar[2] * ar[1])


def det(mat):
    y = 0
    for j in range(0, len(mat[0])):
        y = y + minor(mat, 0, j)
    return y


def transpose(mat):
    arr = zeros((len(mat[0]), len(mat)))

    for i in range(len(arr)):
        for j in range(len(arr[0])):
            arr[i][j] = mat[j][i]
    return arr


def cof(mat):
    arr = []
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            arr.append(minor(mat, i, j) / (mat[i][j]))
    y = reshape(arr, (len(mat), len(mat)))
    return y


def multi(mat1, mat2):
    if len(mat1[0]) == len(mat2):
        new_arr = []
        for i in range(len(mat1)):
            for j in range(len(transpose(mat2))):
                y = array(mat1[i]) * array(transpose(mat2)[j])
                k = sum(y)
                new_arr.append(k)
    else:
        print("multiplication is not possible")
    return array(new_arr).reshape(len(mat1), len(mat2[0]))


def inverse_matrix(mat):
    if det(mat) != 0:
        y = transpose(cof(mat)) / det(mat)
    else:
        print("Inverse Matrix dose not exist")
    return y
# a = [[10, -2, -1, -1], [-2, 10, -1, -1], [-1, -1, 10, -2], [-1, -1, -2, 10]]
# b = [[3], [15], [27], [-9]]
a = [[6, 1, 1], [1, 4, -1], [1, -1, 5]]
b = [[20], [6], [7]]
r = inverse_matrix(a)
y = multi(r, b)
print (y)
