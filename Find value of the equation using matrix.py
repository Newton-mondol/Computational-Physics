import numpy as np

a = np.zeros((3, 3))  # This will store the coefficients of the variables as a 3x3 numpy array
x = np.zeros((3, 1))  # This stores the values of the variables as a 3x1 numpy array
b = np.zeros((3, 1))  # This will store what the equations are equal to as a 3x1 numpy array
varNames = ["x", "y", "z"]

for i in range(3):
    for j in range(3):
        a[i][j] = int(input("What is the " + str(i + 1) + "th coefficient of " + str(varNames[j]) + "? "))
    b[i][0] = -int(input("What is the " + str(i + 1) + "th equation equal to? "))


A = np.append(a, b, axis=1)


def f(A):
    for m in range(len(A) - 1):
        for i in range(m + 1, len(A)):
            x = A[i][m];
            for j in range(m, len(A[0])):
                A[i][j] = A[i][j] - (A[m][j] * x / A[m][m]);
                

    return A;



a = f(A)


z = (-a[2][3] / (a[2][2]))

y = ((1.0 / a[1][1]) * ((-(a[1][3])) - ((a[1][2])) * z))

x = (((-(a[0][3])) - ((a[0][1]) * y) - (a[0][2] * z))) * (1.0 / a[0][0])

print("The value of X is : {}\nThe value of Y is : {}\nThe value of Z is : {}\n".format(x, y, z));
