#WAP to to check whether a given post is talking about "Harry" or not

post = input("Enter the Post : ")
name = "Harry"
if ( name.lower() in post.lower()):
  print("YES")
else:
  print("No")
