from time import sleep
from selenium.webdriver import Firefox
from selenium.webdriver.common.alert import Alert

browser = Firefox()

browser.get('http://selenium.dunossauro.live/aula_11_a')
sleep(3)

alerta = Alert(browser)
# alerta = browser.switch_to.alert # NoAlertPresentException

browser.find_element_by_id('all').click()

alerta.accept() # alerta
alerta.send_keys('Eduardo') # prompt
alerta.accept()  # prompt
alerta.accept() # confirm
