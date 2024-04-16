# Sort a list without using sort keyword

list1 = [76, 23, 45, 12, 54, 9]


len1 = len(list1)
for i in range(len1):
  for j in range(len1 - 1):
    if list1[j] > list1[j+1]:
      temp = list1[j]
      list1[j] = list1[j+1]
      list1[j+1] = temp



print(list1)

