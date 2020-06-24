from selenium.webdriver import Firefox
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import (
    visibility_of_any_elements_located,
    visibility_of_all_elements_located
)
url = 'https://selenium.dunossauro.live/aula_10_b.html'

browser = Firefox()

browser.get(url)

wdw = WebDriverWait(browser, 60)

locator = (By.TAG_NAME,'h1')


wdw.until(
    visibility_of_any_elements_located(locator),
    'h1 não foi encontrado na página. Espera de 60seg.'
)

print('h1 disponível')
