# """
# Given an array of integers, find the GCD of factorials of all elements of the array.
# Input:
#     4
#     3 4 8 6
#     where:
# First line represents the number of elements in the array.
# Second line represents the elements in the array.
# Output:
#     6
# Explanation: We have 3!=6, 4!=24, 8!=40320, and 6!=720. Now GCD of 6, 24, 40320, and 720 = 6, hence the output 6.
# """
size = int(input())
n=0
array = []
for e in input().split():
    if n<size:
        array.append(int(e))
        n = n+1

def fact( n ):
    if n==1:
        return 1
    else:
        return n * fact(n-1)

list1=[]
for element in array:
    list1.append(fact(element))

def find_gcd(x, y): 
    while(y): 
        x, y = y, x % y 
  
    return x 
    
num1=list1[0] 
num2=list1[1] 
gcd=find_gcd(num1,num2) 
  
for i in range(2,len(list1)): 
    gcd=find_gcd(gcd,list1[i]) 
      
print(gcd)

#done