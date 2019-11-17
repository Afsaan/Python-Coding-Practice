"""
Given an array of integers, find another integer such that, if all the elements of the array are subtracted individually from that number, then the sum of all the differences should add to 0. If any such integer exists, print its value otherwise print '-1'.
Input:
    3
    1 2 3

    where:

First line represents the number of elements in the array.
Second line represents the elements in the array.
 
Output:

    2
Explanation: Substracting all the elements of arrays from 2, The sum of difference is: 1 + 0 + (-1) = 0.
"""

size = int(input())
list = input().split()
list = [int(e) for e in list]
sum = 0

for element in list:
    sum=sum+element

number = sum//size

if sum%size == 0 and size*number == sum:
    print(number)
else:
    print("-1")

#done
