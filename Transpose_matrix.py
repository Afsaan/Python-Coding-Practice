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

rows = int(input("enter the number of rows"))
column = int(input("enter the number of column"))

array=[]
for i in range (rows):
    for j in range (column):
        element = int(input("enter the element"))
        array.append(element)
    print("\n")

print(array)