#Generators
#WAP to generate top 10 squares using generator functions.

def top_ten():

    num = 1
    while(num <= 10):
        sq= num * num
        num = num + 1
        yield sq

val = top_ten()

for i in val:
    print(i)
