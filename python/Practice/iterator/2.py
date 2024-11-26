''' Code to show that list, tuple, sets are not iterators -> It will throw an error that list is not a iterator  '''

list1 = ['Kush','Singh',10,10]
it = iter(list1)
print(next(it))
print(next(it))
print(next(it))
print(next(list1))
