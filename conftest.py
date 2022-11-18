import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time


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


def search_url_links():
    browser = webdriver.Chrome()
    browser.get('https://www.cbr.ru/')
    time.sleep(2)
    url_links = []
    button = browser.find_element(By.XPATH, '/html/body/header/div[5]/div/div/div[1]/div/div[1]/div/div')
    button.click()
    time.sleep(2)
    for locator in ['#menu_content_Activity a', '#menu_content_FinancialMarkets a', '#menu_content_Documents a',
                    '#menu_content_AboutBank a', '#menu_content_Services a']:
        for link in browser.find_elements(By.CSS_SELECTOR, locator):
            url_links.append(link.get_attribute('href'))
    return url_links
