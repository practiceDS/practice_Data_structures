#Inner Class

class Student:

    def __init__(self,name,rollno):
        self.name = name
        self.rollno = rollno
        #creating object inside a class
        self.lap = self.Laptop()

    def show(self):
        print(self.name,self.rollno)
        self.lap.show() 

    class Laptop:
        def __init__(self):
            self.ram = "6GB"
            self.processor = "I7"

        def show(self):
            print(self.ram,self.processor)


s1 = Student("Kushagra",066)
s2 = Student("Divya",067)

s1.show()

#creating object of inner class outside the class

lap = s1.Laptop()
lap.show()
