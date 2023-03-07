#WAP to find the factorial of a given number
fact = 1
num = int(input("Enter the number : "))
while (num != 0):
  fact = fact * num
  num = num -1

print("Factorial of number is ",fact)
