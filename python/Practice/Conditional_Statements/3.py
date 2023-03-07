#WAP to detect the Spams

text=input("Enter text : ")

if("make a lot of money" in text):
  spam = True
else:
  spam = False

if("buy now" in text):
  spam = True
else:
  spam = False

if("subscribe this" in text):
  spam = True
else:
  spam = False

if("click this" in text):
  spam = True
else:
  spam = False

if(spam):
  print("This is a Spam")
else:
  print("Its not a Spam")
