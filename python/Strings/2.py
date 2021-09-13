#Reverse the words

string = "I am a python programmer"

word = string.split(' ')
print(word)

word1 = list(reversed(word))
print(word1)

print(" ".join(word1))
