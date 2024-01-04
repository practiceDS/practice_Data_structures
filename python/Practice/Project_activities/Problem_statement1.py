#CustomTypeError class required to raise exception, if user enters value other than string

class CustomTypeError(Exception) :
  def __init__(self,x):
    self.data_type = x
  def __str__(self):
    return f"{self.data_type} not allowed. Only use String"

class FreqMapper():
#Constructor method to assign values to the variables.
  def __init__(self,value,my_dict,case_sensitive = False):
      self.value = value
      self.my_dict = my_dict
      self.case_sensitive = case_sensitive
# Function used to count and convert it into a dictionary. Handles cases for
# both case sensitive and insensitive approach entered by the user
  def fun(self):
    i = 0
    if(not isinstance(self.value,str)):
      raise CustomTypeError(type(self.value))
#Condition to checkfor case sentivity.
    if (self.case_sensitive == False):
      self.value = self.value.lower()
    while (i < len(self.value)):
      self.my_dict[self.value[i]] = self.value.count(self.value[i])
      i = i + 1
    return (self.my_dict)

