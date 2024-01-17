''' Generate a fibonacci series using generator '''

def generator(n):
  n1 = 0
  n2 = 1
  for i in range(n):
    yield n1
#    n1, n2 = n2, n1 + n2
    temp = n1
    n1 = n2
    n2 = temp + n2
count = int(input("How many terms "))

print("Fibonacci series: ")
print(list(generator(count)))
