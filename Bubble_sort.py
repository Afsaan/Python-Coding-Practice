"""
Given an array of integers, sort the array in ascending/descending order by using bubble sort algorithm. 
Write a program to accept 3 parameters, an array A of integers, size of the array N and sorting order O (0 or 1).
Note: 
    0 represents ascending order.
    1 represents descending order.
Input 
    0 
    9 
    4 3 6 8 9 2 1 5 7 
Where, 
First line represents the type of ordering. 
Second line represents the size of the array. 
Third line represents array elements.  
Output 
    1 2 3 4 5 6 7 8 9 
"""

# Bubble Sort
def solution(L,size,option):
    if option == 0:
        for i in range(size):
            for j in range(size):
                if L[i]<L[j]:
                    L[i],L[j] = L[j],L[i]
        
        return L

    elif option ==1:
        for i in range(size):
            for j in range(size):
                if L[i]>L[j]:
                    L[i],L[j] = L[j],L[i]
                    
        return L
    
    else:
        print("wrong question")
        
O=int(input("Enter the choice 0-->Ascending and 1--> Descending"))       
N=int(input("Enter the size of an array"))
L=[]
n=0
for e in input().split():
    if(n<N):
        L.append(int (e))
        n+=1
a = solution(L,N,O)
str = " ".join(str(e) for e in a)
print("Sorted array is",str,end='')

