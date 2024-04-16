# WAP to check whther a string is pallindrome or not.
#  ABCDCBA (Pallindrome)
#  ABDA (Not Pallindrome)

str1 = "ABCDCBA"
str2 = str1[::-1]
str3 = "ABDA"
str4 = str3[::-1]
print(str1)
print(str2)
print(str4)
if str1 == str2:
  print("string is pallindrome")
if str3 == str4:
  print("string is pallindrome")
else:
  print("Its not pallindrome")
