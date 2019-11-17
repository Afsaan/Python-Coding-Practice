"""
Given an array of size N and the task is to find the Coefficient of variation. The coefficient of variation is the ratio of standard deviation and mean.
Input:
    5
    60.25 62.38 65.32 61.41 63.23

where:

First line represents the number of elements in the array.
Second line represents the elements in the array.
Output:
    0.0307144
Explanation:
Coefficient of Variation = (Standard deviation / mean).
In the array  {60.25, 62.38, 65.32, 61.41, 63.23}
mean = 62.518
Standard Deviation = 1.9202
Coefficient of Variation = (Standard deviation / mean) = 1.9202 / 62.518 = 0.0307144.
Hence the output 0.0307144.
"""

size = int(input())


elements = input()
list = elements.split()

list = [ float(e) for e in list]

mean = 0 
for i in list:
    mean = mean + i

mean = mean/size
print(list,mean)

sum = 0
for i in list:
    sum  = sum + pow(i-mean,2)

derivative = pow((sum)/(size-1),1/2)

COV = derivative/mean

print(round(COV,7))

print(derivative)

#done