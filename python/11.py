#Global variable vs local variable
#Changing global variable inside function. -- global keyword
#Keeping global and local variable in a same function -- globals keyword -->used to fetch the global variabled
a = 10

def fun():
    globals()['a'] = 20
    print("Inside fun a = %d",a)

fun()
print("Outside fun a = %d",a)
