# WAP to print FizzBuzz. What is FizzBuzz String, If a number is divisble by 3,
# print "Fizz", if a number is Divisible by 5, print "Buzz" and if a number is
# divisible by both 3 and 5 print "FizzBuzz".


num = int(input("Enter the number "))
gen_list = []
for i in range(1,num+1):
  if ((i % 3 == 0) and (i % 5 == 0)):
    gen_list.append("FizzBuzz")
  elif (i % 5 == 0):
    gen_list.append("Buzz")
  elif (i % 3 == 0):
    gen_list.append("Fizz")
  else:
    gen_list.append(str(i))

complete_str = ' '.join(gen_list)
print(complete_str)
