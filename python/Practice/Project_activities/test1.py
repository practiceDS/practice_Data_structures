import Problem_statement1


def test_case_insensitive():
  my_dict = dict()
  s1 = Problem_statement1.FreqMapper("TestT",my_dict)
  print(s1.fun())


def test_case_sensitive():
  my_dict = dict()
  s1 = Problem_statement1.FreqMapper("TesttT",my_dict,True)
  print(s1.fun())

def test_incorrectInput():
  my_dict = dict()
  s1 = Problem_statement1.FreqMapper(24.0,my_dict)
  print(s1.fun())

test_case_insensitive()
test_case_sensitive()
test_incorrectInput()

