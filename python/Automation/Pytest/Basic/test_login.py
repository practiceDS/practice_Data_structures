import pytest
@pytest.mark.kushagra
def  testLogin():
    print("Login is successfull")

@pytest.mark.skip
def  testLogoff():
    print("LogOff is successfull")