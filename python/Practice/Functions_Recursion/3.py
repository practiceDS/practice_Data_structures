# WAP a recursive program to calculate sum of 1st n natural numbers

def sum(n):
  if(n == 1):
    return 1

  return n + sum(n-1)

num = int(input("Enter the number : "))
print(sum(num))
