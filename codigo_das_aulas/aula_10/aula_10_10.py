from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import (
    text_to_be_present_in_element,
)
url = 'https://selenium.dunossauro.live/aula_10_d.html'

browser = Firefox()

browser.get(url)

wdw = WebDriverWait(browser, 50)

locator_h4 = (By.TAG_NAME, 'h4')

locator_nome = (By.CSS_SELECTOR, 'input[name="nome"]')

wdw.until(
    text_to_be_present_in_element(
        locator_h4,
        'Digite'
    )
)

browser.find_element(*locator_nome).send_keys('Fausto')
