from selenium.webdriver import Firefox
from selenium.webdriver.common.alert import Alert

browser = Firefox()

browser.get('http://selenium.dunossauro.live/aula_11_a')

browser.find_element_by_id('prompt').click()

alerta = Alert(browser)

alerta.accept()
alerta.dismiss()
