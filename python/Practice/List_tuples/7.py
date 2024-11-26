# Python program to find all possible pairs with given sum
# Ex - [1, 5, 3, 7, 9], K = 12
# Output - [(5, 7), (3, 9)]


list1 = [1,5,3,7,9]
num = 12
pair = ()
list2 = []
length = len(list1)
for i in range(length):
  for j in range(i,length):
    if (list1[i] + list1[j] == num):
      b = (list1[i],list1[j])
      list2.append(b)

print(list2)
      

