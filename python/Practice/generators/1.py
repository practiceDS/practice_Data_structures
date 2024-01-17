def generator():
  print("Hello")
  yield 5

  return

  print("Hi")
  yield 10

  print("Bye")
  yield 15


get = generator()
print(next(get))
print(next(get))
print(next(get))
print(next(get))
