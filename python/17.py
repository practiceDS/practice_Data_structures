#Inheritance, if you create an object of subclass it will first try to find the object of subclass, if its not present, then it call the init of super class.
#Note :- there is a super() method used to call both the constructor of both sub class and super class

#MRO(Method Resolution order) :- In case of multiple Inheritance, the inherit order will be from left to right always

class A(object):

    def __init__(self):
        print("This is in A class")

    def feature1(self):
        print("This is feature 1")



class B(object):

    def __init__(self):
        print("This is in B class")

    def feature2(self):
        print("This is feature 2")


class C(B,A):

    def __init__(self):
        super(C,self).__init__()
        print("This is in C class")

    def feature2(self):
        print("This is feature main")


a1 = C()
a1.feature2()
