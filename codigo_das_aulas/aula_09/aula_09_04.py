from functools import partial
from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import (
    WebDriverWait
)


def esperar_elemento(by, elemento, webdriver):
    print(f'Tentando encontrar "{elemento}" by {by}')
    if webdriver.find_elements(by, elemento):
        return True
    return False


esperar_botao = partial(
    esperar_elemento, By.CSS_SELECTOR, 'button'
)

url = 'https://selenium.dunossauro.live/aula_09_a.html'

driver = Firefox()

wdw = WebDriverWait(driver, 10)

driver.get(url)

wdw.until(esperar_botao, 'Deu ruim')

driver.find_element_by_css_selector('button').click()

wdw.until(
    partial(esperar_elemento, 'id', 'finished'),
    'A mensagem de sucesso não apareceu'
)

sucesso = driver.find_element_by_css_selector('#finished')

assert sucesso.text == 'Carregamento concluído'
