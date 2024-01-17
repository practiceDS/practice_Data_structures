''' WAP to add two numbers using decorators '''

def my_decorator(func):
  def wrapper(*args,**kwargs):
    print("Parameters added",args)
    result = func(*args,**kwargs)
    print("Final Results",result)
  return wrapper

@my_decorator
def add(x,y):
  return x + y


add(2,3)


