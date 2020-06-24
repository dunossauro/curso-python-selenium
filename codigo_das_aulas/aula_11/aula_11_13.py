from time import sleep
from selenium.webdriver import Firefox
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.expected_conditions import (
    frame_to_be_available_and_switch_to_it,
    element_to_be_clickable
)


browser = Firefox()
wdw = WebDriverWait(browser, 60)

browser.get('http://selenium.dunossauro.live/aula_11_d')

wdw.until(
    frame_to_be_available_and_switch_to_it(
        ('name', 'iframe')
    )
)

wdw.until(
    element_to_be_clickable(('name', 'nome'))
)

browser.find_element_by_id('nome').send_keys('Eduardo')
