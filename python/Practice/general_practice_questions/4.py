# How to find out the factorial of a given number.

num = int(input("Enter the number to find factorial "))
fact = 1
while (num !=0):
  fact = fact * num
  num = num - 1


print("Output:- ",fact)
