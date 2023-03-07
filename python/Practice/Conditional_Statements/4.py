#WAP to find whether a username contains less than 10 characters

user = input("Enter the username : ")
count = len(user)
if(count < 10):
  print("Less than 10")
else:
  print("Greater than 10")


