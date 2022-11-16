from selenium.webdriver.common.by import By


def test_search_pdf_on_main_page(browser):
    link = 'https://www.cbr.ru/'
    browser.get(link)
    links_have_href = browser.find_elements(By.CSS_SELECTOR, 'a[href]')
    links_pdf = []
    for link in links_have_href:
        href = link.get_attribute("href")
        if '.pdf' in href:
            links_pdf.append(href)
            print(href)





