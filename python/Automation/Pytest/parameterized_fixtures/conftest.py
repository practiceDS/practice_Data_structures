import pytest
@pytest.fixture(scope='session',autouse=True)
def tc_setup(browser):
    if browser == 'chrome':
        print("Open the application in chrome")
    else:
        print("open application in firefox")
    print("Login to the application")
    yield
    print("Log off from the application")
    print("Close the browser")


def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture(scope='session',autouse=True)
def browser(request):
    return request.config.getoption("--browser")