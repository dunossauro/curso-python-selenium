from selenium.webdriver import Firefox
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import (
    staleness_of
)
url = 'https://selenium.dunossauro.live/aula_10_b.html'

browser = Firefox()

browser.get(url)

wdw = WebDriverWait(browser, 60)

wdw.until(
    staleness_of(
        browser.find_element_by_tag_name('button')
    )
)

element.click()

p = browser.find_element_by_tag_name('p')

assert 'quei' in p.text
