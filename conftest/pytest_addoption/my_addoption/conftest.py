import pytest
from selenium import webdriver

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()

def pytest_addoption(parser):
    parser.addoption("--language", action="store", default="ru",
                     help="Specify the language for the tests")

@pytest.fixture(scope="session")
def language(request):
    return request.config.getoption("language")