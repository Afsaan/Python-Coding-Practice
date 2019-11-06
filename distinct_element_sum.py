"""
Given an array of N integers, find the sum of all the distinct elements of the array.

Elements of the array would be in the range of 1 to N.
Input:
    9
    5 1 2 4 6 7 3 6 7
where:
First line represents the number of elements in the array.
Second line represents the elements in the array.
Output:
    28
Explanation: The distinct elements in the array are 1, 2, 3, 4, 5, 6, and 7  Hence their sum: 1+2+3+4+5+6+7 = 28, so the output is 28.
"""

size = int(input("Enter the size of the element"))

array =[]

for i in range(size):
    element = int(input("enter the element"))
    array.append(element)

print(array)

new_array=[]
for i in array:
    if i in new_array:
        continue
    new_array.append(i)

print(new_array)  # elemnt without the duplicate

sum=0
for i in new_array:
    sum = sum +i

print(sum)  # sum of all the element in the array
    
    