from selenium.webdriver import Firefox

browser = Firefox()

browser.get('http://selenium.dunossauro.live/aula_11_a')

browser.find_element_by_id('alert').click()

alerta = browser.switch_to.alert

alerta.accept() # Confirma, clica no OK
alerta.dismiss() # Confirma, clica no OK
