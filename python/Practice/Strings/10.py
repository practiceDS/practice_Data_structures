# Longest Palindrome Substring eg :- Input: str = “forgeeksskeegfor” 
# Output :- "geeksskeeg"



def check_palindrome(s,i,j):
  while i < j:
    if s[i] != s[j]:
      return False

    i = i + 1
    j = j - 1

  return True


def longest_palindromic_substring(s):
  start = 0
  max_len = 1
  n = len(s)

  for i in range(n):
    for j in range(i,n):
      if check_palindrome(s,i,j) and (j - i + 1) > max_len:
        start = i
        max_len = j - i + 1


  return s[start:start + max_len]



print(longest_palindromic_substring("forgeeksskeegfor"))
