#Types of methods :- Instance, Class and Static methods.

class Student:

    school_name = "DPS"

#instance method
    def __init__(self,m1,m2,m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3


    def avg(self):
        return (self.m1 + self.m2 + self.m3)/3

#Class methods
    @classmethod
    def info(cls):
        return cls.school_name

#Static method
    @staticmethod 
    def info1():
        print("This is a static method\n")

s1 = Student(12,13,14)
print(s1.avg())
print(Student.info())
Student.info1()

