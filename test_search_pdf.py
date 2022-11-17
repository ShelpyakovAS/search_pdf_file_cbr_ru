from selenium.webdriver.common.by import By
import pytest

'''browser.get('https://www.cbr.ru/')
url_links = []
for locator in ['#menu_content_Activity a', '#menu_content_FinancialMarkets a', '#menu_content_Documents a',
                '#menu_content_AboutBank a', '#menu_content_Services a']:
for link in browser.find_elements(By.CSS_SELECTOR, locator):
        url_links.append(link.get_attribute('href'))'''
url_links = []


@pytest.mark.parametrize('link', url_links)
def test_search_pdf_on_main_page(browser, link):
    browser.get(link)
    links_have_href = browser.find_elements(By.CSS_SELECTOR, 'a[href]')
    links_pdf = []
    for link in links_have_href:
        href = link.get_attribute("href")
        if '.pdf' in href:
            links_pdf.append(href)
            print(href)


# #menu_content_Activity a
# #menu_content_FinancialMarkets a
# #menu_content_Documents a
# #menu_content_AboutBank a
# #menu_content_Services a