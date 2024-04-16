#WAP to check whether the number input is armstrong number.
import math

def check_armstrong(num):
  num_list = list()
  arm_num = 0
  while(num > 0):
    rem = int(num % 10)
    num_list.append(rem)
    num = int(num / 10)
  length = len(num_list)
  for i in num_list:
    arm_num = int(math.pow(i,length)) + arm_num
  return arm_num

num = int(input("Enter the number"))
validate_armstrong = check_armstrong(num)
if (validate_armstrong == num):
  print("Number is armstrong number")
else:
  print("Number is not armstrong number")
