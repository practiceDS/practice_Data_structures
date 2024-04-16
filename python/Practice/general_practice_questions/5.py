# How to check if a number is prime number or not

num = int(input("Enter the number:- "))
mid = int(num/2)
flag = 1
while(mid > 1):
  if (num % mid == 0):
    flag = 0
  mid = mid - 1

if (flag == 1):
  print("Prime number")
else:
  print("Not a prime number")

