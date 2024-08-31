import pytest
from selenium import webdriver

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()

def pytest_generate_tests(metafunc):
    if "language" in metafunc.fixturenames:
        metafunc.parametrize("language", ["ru", "en-gb"])