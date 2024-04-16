# WAP to find second largest in the List without sort.

list1 = [70,11,20,4,100]

max_num = max(list1)
print(max_num)
list1.remove(max_num)
print("second largest number in the list",max(list1))
