from selenium.webdriver import Firefox
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import (
    url_contains,
    url_matches
)
url = 'https://selenium.dunossauro.live/aula_10_c.html'

browser = Firefox()

browser.get(url)

wdw = WebDriverWait(browser, 10)

links = browser.find_elements_by_css_selector('.body_b a')
links[1].click()

wdw.until(
    url_contains('selenium'),
)

wdw.until(
    url_matches('http.*live'),
)
