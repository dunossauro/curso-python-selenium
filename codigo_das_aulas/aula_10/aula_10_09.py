from selenium.webdriver import Firefox
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import (
    title_is,
    title_contains
)
url = 'https://selenium.dunossauro.live/aula_10_c.html'

browser = Firefox()

browser.get(url)

wdw = WebDriverWait(browser, 10)

links = browser.find_elements_by_css_selector('.body_b a')
links[0].click()

wdw.until(
    title_contains('Aula'),
)

wdw.until(
    title_is('Aula 10b'),
)
