from selenium.webdriver import Firefox
from selenium.webdriver.common.alert import Alert

browser = Firefox()

browser.get('http://selenium.dunossauro.live/aula_11_a')

browser.find_element_by_id('alert').click()

alerta = Alert(browser) # Liadar com erros

alerta = browser.switch_to.alert # Não lida com erros


alerta.accept() # Confirma, clica no OK
alerta.dismiss() # Confirma, clica no OK
