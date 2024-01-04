#Check if String Contains Substring in Python
'''
Input: Substring = "geeks" 
            String="geeks for geeks"
Output: yes
Input: Substring = "geek"
           String="geeks for geeks"
Output: yes
Explanation: In this, we are checking if the substring is present in a given string or not.
'''

import sys


if len(sys.argv) != 3:
  print("Number of arguments are wrong")
  sys.exit()


string = str(sys.argv[1])
substring = str(sys.argv[2])

list1 = string.split(" ")

if substring in list1:
  print("yes")
else:
  print("no")

## Best approach
if string.find(substring) >= 0: 
  print("yes")
else:
  print("no")
