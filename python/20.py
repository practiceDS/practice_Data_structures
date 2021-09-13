#Iterators in python is an object that is used to iterate over iterable objects like lists, tuples, dicts, and sets. The iterator object is initialized using the iter() method. It uses the next() method for iteration.

num = [1,3,5]

it = iter(num)

for it in num:
    print(it)
