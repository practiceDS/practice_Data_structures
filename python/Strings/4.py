#How to Remove Letters From a String in Python.
##  Input: 'Geeks123For123Geeks'
##  Output: GeeksForGeeks
##  Explanation: In This, we have removed the '123' character from a string.

string = "Geeks123For123Geeks"
string1 = string.replace("123","")
print(string1)
print(string)
