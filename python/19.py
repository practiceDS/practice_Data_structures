#Abstract Classes :- Abstract classes are the class which have atleast one abstarct method , by default python doesn't support
#abstract classed to perform that we need to import ABC module :- Abstract Base Class
#Abstract Method :- Method which only have declarration not definition

from abc import ABC ,abstractmethod

class Computer(ABC):
    @abstarctmethod
    def process(self):
        pass


class Laptop(Computer):

    def process(self):
        print("Laptop")


c1 = Laptop()
