
# As I solve this equation by echelon form , the equation will be  Ax - B =0
# equations : ax + by + cy = d ;   a_1x + b_1y + c_1y = d_1;   a_2x + b_2y+ c_2 z = d_2
#             ax + by + cy -d = 0; a_1x + b_1y + c_1y - d_1 =0; a_2x + b_2y+ c_2 z - d_2 =0
# the matrics form of the equation will be,
# A = [[a ,b ,c], [a_1 , b_1, c_1],[a_2, b_2 ,c_2]]
# B = [d , d_1 , d_2]
#  so, the matrix:  [[a ,b ,c , -d], [a_1, b_1, c_1, -d_1] , [a_2, b_2, c_2, -d_2]]
# At first ,define a function. then a matrix operation is performed in this function.Here m is the operation number that runs n-1 times.
# Then secod loop is  row accessing loop .Third loop works as column accessing loop.
# Here , m = diagonal matrix first element.
# 1st row multiplying by second rows first element - 2nd row multiplying by first rows first element.
# then the row echelon operation matrix will be : [[a00, a01, a02, a03],[0,a11,a12, a13],[0,0,a22,a23]]

def f(matrix):

    for m in range(len(matrix) - 1):
        for i in range(m + 1, len(matrix)):
            x = matrix [i][m];
            for j in range(m, len(matrix[0])):

                matrix[i][j] = matrix[m][m] * matrix[i][j] - matrix[m][j] * x;

# then from the reduced row echelon form ,write:
# a22 z = - a23 ; or, z = - (a23/a22)
# a11 y + a12 z = - a13; or, y = (1/a11)*(-a13 - a12 z)
# a00 x + a01y + a02z = -a03; x = (-a03 - a01y - a02z)
# this code is valid for 3*3 matrix .
    z = (-(matrix[2][3]) / (matrix[2][2]))

    y = ((1.0 / matrix[1][1]) * ((-(matrix[1][3])) - ((matrix[1][2])) * z))

    p = (((-(matrix[0][3])) - ((matrix[0][2]) * z) - (matrix[0][1] * y))) * (1.0 / matrix[0][0])

    print("The value of x is : {}\nThe value of y is : {}\nThe value of z is : {}\n".format(p,y,z));



a = [[2.0,1.0,-1.0,-8],[-3.0,-1.0,2.0,13.0],[-2.0,1.0,2.0,3.0]]

f(a)



b = [[1.0 , 2.0 ,-1.0 ,-6.0],[3.0,8.0,9.0,-10.0],[2.0,-11.0,2.0,2.0]]


f(b)
