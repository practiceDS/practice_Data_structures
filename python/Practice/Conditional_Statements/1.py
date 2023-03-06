#WAP to to find greatest of 4 numbers entered by the user

a = int(input("Enter number 1: "))
b = int(input("Enter number 2: "))
c = int(input("Enter number 3: "))
d = int(input("Enter number 4: "))

if (a>b):
  b=a
elif(b>c):
  c=b
elif(c>d):
  d=c

print("Greatest number is :",d)

  
