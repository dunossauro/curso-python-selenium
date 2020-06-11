from functools import partial
from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import (
    WebDriverWait
)


class EsperarElementoNotClick:
    def __init__(self, locator):
        self.locator = locator

    def __call__(self, webdriver):
        elementos = webdriver.find_elements(*self.locator)
        if elementos:
            return 'unclick' in elementos[0].get_attribute('class')
        return False


def esperar_elemento(by, elemento, webdriver):
    if webdriver.find_elements(by, elemento):
        return True
    return False


locator = (By.CSS_SELECTOR, 'button')
esperar_botao = EsperarElementoNotClick(locator)


url = 'https://selenium.dunossauro.live/aula_09.html'

driver = Firefox()

wdw = WebDriverWait(driver, 10)

driver.get(url)

wdw.until_not(esperar_botao, 'Deu ruim')

driver.find_element_by_css_selector('button').click()

wdw.until(
    partial(esperar_elemento, 'id', 'finished'),
    'A mensagem de sucesso não apareceu'
)

sucesso = driver.find_element_by_css_selector('#finished')

assert sucesso.text == 'Carregamento concluído'
