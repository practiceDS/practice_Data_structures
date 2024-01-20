import pytest
@pytest.fixture(scope="session",autouse=True)
def testSetup():
    print("Open the application")
    print("Login to the application")
    yield
    print("Log off from the application")
    print("Close the browser")
