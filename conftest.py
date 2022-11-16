import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--browser', action='store', default='Chrome',
                     help="Choose language: Chrome or Firefox")


@pytest.fixture(scope="function")
def browser(request):
    selected_browser = request.config.getoption("--browser")
    options = Options()
    print("\nstart browser for test..")
    if selected_browser == 'Firefox':
        browser = webdriver.Firefox(options=options)
    else:
        browser = webdriver.Chrome(options=options)
    yield browser
    print("\nquit browser..")
    browser.quit()