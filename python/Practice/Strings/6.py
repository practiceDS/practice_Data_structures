#Maximum repeating characters in string. Input:- GeeksforGeeks
# Output :-e


input_string = "GeeksforGeeks"
# Initialize array with 256 length.
ascii_list = [0] * 256
for i in input_string:
  ascii_list[ord(i)] = ascii_list[ord(i)] + 1

max_index = ascii_list.index(max(ascii_list))
print("Maximum occuring character in String is :- ",chr(max_index))

