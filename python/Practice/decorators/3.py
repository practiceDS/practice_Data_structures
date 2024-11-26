
def my_decorator(fun1):
  def wrapper(*args,**kwargs):
    print("Parameters",args)
    result = fun1(*args,**kwargs)
    print("Result",result)
  return wrapper

@my_decorator
def add(x,y):
  return x + y


add(2,3)
