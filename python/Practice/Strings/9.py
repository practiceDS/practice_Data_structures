# Input : ""The sky is blue""
# Output: ""blue is sky the""


str1 = "The sky is blue"
list1 = str1.split()
print(' '.join(list1[::-1]))

