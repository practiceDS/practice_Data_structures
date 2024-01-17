'''Write a simple program to define decorators.'''

def my_decorator(func):
  def wrapper():
    print("Good Morning")
    func()
    print("Exiting from the function")
  return wrapper


@my_decorator
def func1():
  print("hello")



func1()




