#WAP to find sum of first n natural numbers

num = int(input("Enter the number till which we want to find the sum : "))
i = 0
total = 0
while (i <= num):
  total = total + i
  i = i + 1
print("The sum of natural numbers ",total)
