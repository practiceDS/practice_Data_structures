#Iterators in python is an object that is used to iterate over iterable objects like lists, tuples, dicts, and sets. The iterator object is initialized using the iter() method. It uses the next() method for iteration.

# Creating your own Iterators.

class val:

    def __init__(self):
        self.num = 1


    def __iter__(self):
        return self

    def __next__(self):
        if(self.num <= 10):
            val = self.num
            self.num = self.num + 1
            return val

        else:
            raise StopIteration()



v1 = val()

for i in v1:
    print(i)

