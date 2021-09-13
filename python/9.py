#Arguments
# Position,keyword,default,variable length

def person(name,age):
    print(name)
    print(age)



def person1(name,b = 18):
    print(name)
    print(b)

def sum (*b):

    c=0
    for i in b:
        c = c + i

    print(c)


#position
person("kushagra",29)
#keyword
person(age=29,name="kushagra1")
#default
person1("Divya")
#variable length
sum(1,2,3)
