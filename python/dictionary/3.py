#Concatenate two dictionary


dict1 = {1: "Kushagra1", 2: "Kushagra2", 3: "Kushagra3" }
dict2 = {4: "Kushagra4", 5: "Kushagra5", 6: "Kushagra6" }

dict3 = dict(dict1.items() + dict2.items())
print(dict3)
