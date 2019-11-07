"""
Given an order of a square matrix, print Identity matrix of the entered order. An Identity Matrix is a square matrix in which all the elements of the principal or main diagonal are 1’s and all other elements are zeros.
Input:
    4
where
Input represents the order of the matrix required.
 
Output:

    1 0 0 0

    0 1 0 0

    0 0 1 0

    0 0 0 1

Explanation: Here the Identity matrix of order 4 is printed as per the definition main diagonal elements are '1' and all other than that are '0'.

Assumptions:

Order of a matrix can be in the range 1 to 1000.
A square matrix of order k contains k*k elements.
"""

n  = int(input(""))

matrix = [[0 for j in range(n)]for i in range(n)]

for i in range(n):
    for j in range(n):
        if i == j:
            matrix[i][j]="1"
        else:
            matrix[i][j]="0"


for i in range(n):
    a= matrix[i]
    b = " ".join(a)
    print(b)

