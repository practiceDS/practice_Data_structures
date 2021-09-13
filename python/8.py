#Function arguments :- List are mutable in nature
def update(x):
    
    print("id of x = \n",id(x))
    print("id of a = \n",id(a))
    x[1] = 25
    print("id of  after assignemt x = \n",id(x))
    print(x)


a = [10,20,30]
print("id of MAIN a = \n",id(a))
update(a)
print("id of MAIN after update a = \n",id(a))
print(a)
