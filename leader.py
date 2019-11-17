"""
Given an array of integers A. Find all the Leaders in the array.
Display the count of Leaders in an array. 
Input
    5 
    9 0 5 6 4

    Where, 
The first line represents the size of an array. 
The second line represents array elements separated by single space.
Output
    3

Here for the given an array, there are 3 leaders 9, 6 and 4.
"""
size = int(input())

a = input()
list = a.split()

count = 0
for i in range (0,size):
    for j in range(i+1,size):
        if list[i] < list[j]:
            break
    if j == size-1:
        count = count +1

print(count)

#done



            
        

