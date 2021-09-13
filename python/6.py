#Take user from input and create an array and search an element in the array and print its index

from array import *

arr = array('i',[])
print("Enter the len of array\n")

count = int(input())

for i in range(count):
    print("Enter next number\n")
    y = int(input())
    arr.append(y)


print(arr)
    
print("Enter the number to be searched in array\n")
num = int(input())

k=0

for i in arr:
    if(i == num):
        print(k)
        break
    else:
        k = k+ 1
