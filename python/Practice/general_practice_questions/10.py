#''' WAP to print first n fibonaci series  0,1,1,2,3,5....'''

def fibonaci_series(n):
  a = 0
  b = 1
  i = 2
  list1 = list()
  print("Fibonaci series")
  print(a)
  print(b)
  list1.append(a)
  list1.append(b)
  while(i<=n):
    f = a + b
    list1.append(f)
    a = b
    b = f
    i = i + 1
  return list1

n = int(input())
print(fibonaci_series(n))


    

