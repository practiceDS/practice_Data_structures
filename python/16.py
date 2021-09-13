#Inheritance, if you create an object of subclass it will first try to find the object of subclass, if its not present, then it call the init of super class.
#Note :- there is a super() method used to call both the constructor of both sub class and super class


class A(object):

    def __init__(self):
        print("This is in A class")

    def feature1(self):
        print("This is feature 1")



class B(A):

    def __init__(self):
        super(B,self).__init__()
        print("This is in B class")

    def feature2(self):
        print("This is feature 2")



a1 = B()
