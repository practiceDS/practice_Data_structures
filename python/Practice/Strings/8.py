# Compress String
# Input : aabbccddeeee
# Output: a2b2c2d2e4


str1 = "aabbccddeeee"
n = len(str1)
i = 0
list1 = list()
while (i < n -1):
  list1.append(str1[i])
  count = 1
  while((i < n -1) and (str1[i] == str1[i+1])):
    count = count + 1
    i = i + 1
  list1.append(str(count))
  i = i + 1

str3 = ''.join(list1)
print(str3)
