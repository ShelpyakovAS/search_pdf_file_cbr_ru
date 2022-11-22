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
    options.headless = True
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
    url_links = ['https://www.cbr.ru/', ]
    button = browser.find_element(By.XPATH, '/html/body/header/div[5]/div/div/div[1]/div/div[1]/div/div')
    button.click()
    time.sleep(2)
    for locator in ["//*[contains(@class,'inner_links')]//a",
                    "//*[contains(@id,'menu_content_Activity')]//a",
                    "//*[contains(@id,'menu_content_FinancialMarkets')]//a",
                    "//*[contains(@id,'menu_content_Documents')]//a",
                    "//*[contains(@id,'menu_content_AboutBank')]//a",
                    "//*[contains(@id,'menu_content_Services')]//a"]:
        for link in browser.find_elements(By.XPATH, locator):
            url_links.append(link.get_attribute('href'))
    return url_links