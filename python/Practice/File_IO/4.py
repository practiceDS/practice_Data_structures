# Importing BeautifulSoup class from the bs4 module
from bs4 import BeautifulSoup
  
# Opening the html file
HTMLFile = open("test.html", "r")
  
# Reading the file
index = HTMLFile.read()
  
# Creating a BeautifulSoup object and specifying the parser
#S = BeautifulSoup(index, 'lxml')
  
print(index)
