from time import sleep
from selenium.webdriver import Firefox
from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support.expected_conditions import (
#
# )


browser = Firefox()
wdw = WebDriverWait(browser, 60)

browser.get('http://selenium.dunossauro.live/aula_11_d')

# browser.switch_to.frame()

browser.find_element_by_id('nome')
