#WAP using function to find greatest of three numbers

def find_greatest(a,b,c):
  l1 = [a,b,c]
  l1.sort()
  length = len(l1)
  print(l1)
  return l1[length -1]

a = int(input("Enter number 1 : "))
b = int(input("Enter number 2 : "))
c = int(input("Enter number 3 : "))
print(find_greatest(a,b,c))
