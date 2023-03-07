#WAP to check whether a program is pass or fail, if it requires total of 40% and at least 33% in each subject to pass. Assume 3 subjects and take marks as an input from the user.

subject1 = int(input("Enter the marks of Subject 1 :"))
subject2 = int(input("Enter the marks of Subject 2 :"))
subject3 = int(input("Enter the marks of Subject 3 :"))

total = subject1 + subject2 + subject3
avg = total/3

if((subject1 > 33 and subject2 > 33 and subject3 > 33) and avg > 40):
  print("PASS")
else:
  print("FAIL")
