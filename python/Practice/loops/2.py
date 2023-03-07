#WAP to to greet all the person present in the list l1 , which starts with "S"
l1 = ["Harry","Sonam","Sachin","Rahul"]
length = len(l1)
i=0
while (i < length):
#  if(l1[i].startswith("S")):
  if(l1[i][0] == "S"):
    print("Hello " + l1[i])

  i = i + 1

