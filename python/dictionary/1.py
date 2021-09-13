#Merge two list to create a dictionary

key = [1,2,5]
values = ["Kushagra","Kushagra1", "Kushagra2"]
out = dict(zip(key,values))
print(out)

#Adding data to the merge list

out[6] = "Kushagra3"
print(out)

#Deleting data from Dictionary
del out[6]
print(out)
