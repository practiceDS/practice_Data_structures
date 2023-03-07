#WAP to find out whether the number is prime or not

num = int(input("Enter the number : "))
n1 = num / 2
i = 2
Flag = True
while(i <= n1):
  if(num % i == 0):
    Flag = False
    break

  else:
    i = i + 1

if(Flag == False):
  print(num," is not a Prime number")
else:
  print(num," is a Prime number")
