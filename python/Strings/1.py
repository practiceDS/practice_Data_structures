#WAP to check if string is symmetrical and pallindrome
import sys

string = str(sys.argv[1])
print(string)

half = len(string)/2

if (half % 2 == 1):
    first_part = string[half:]
    second_part = string[:half]
else:
    first_part = string[half:]
    second_part = string[:half+1]


if (first_part == second_part):
    print("Strings are symmetrical\n")
else:
    print("Strings are not symmetrical\n")


if (first_part == second_part[::-1]):
    print("Strings are Pallindrome\n")
else:
    print("Strings are not Pallindrome\n")
