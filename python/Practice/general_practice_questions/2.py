# Print first 10 numbers of fibonacci series in python

a = 0
b = 1
num = 0
list1 = []
list1.append(a)
list1.append(b)
length = int(input("Enter the number of enteries in fibonacci series"))
while(num < length - 2):
  c = a + b
  list1.append(c)
  a = b
  b = c
  num = num + 1


print(list1)
