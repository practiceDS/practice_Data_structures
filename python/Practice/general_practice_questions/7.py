# Python Program to raise an exception


def divide(a,b):
  if (b == 0):
    raise Exception("Cannot divide by Zero")
  return a/b

try:
  divide(10,0)
except Exception as e:
  print("An error occured",e)
