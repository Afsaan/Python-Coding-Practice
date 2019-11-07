"""Given a matrix, find the transpose of a matrix. 
Input 
    2 
    4 
    1 2 3 4 
    2 9 -1 2 
Where, 
First line represents the number of rows as M. 
Second line represents the number of columns as N. 
Third line contains matrix elements of 1st row and so on. 
Output 
    1 2 
    2 9 
    3 -1 
    4 2 
"""

rows = int(input())
column = int(input())

x=[]
for i in range(rows):
    string = input()
    t = string.split()
    x.append(t)

T = [[0 for i in range(rows)]for j in range(column)] 
for i in range(column):
    for j in range(rows):
        T[i][j]=x[j][i]
        
for i in range(column):
    a = T[i]
    b = " ".join(a)
    print(b)
