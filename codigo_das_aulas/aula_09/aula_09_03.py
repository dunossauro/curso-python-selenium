from functools import partial
from selenium.webdriver import Firefox
from selenium.webdriver.support.ui import (
    WebDriverWait
)


def esperar_elemento(elemento, webdriver):
    print(f'Tentando encontrar "{elemento}"')
    if webdriver.find_elements_by_css_selector(elemento):
        return True
    return False


esperar_botao = partial(esperar_elemento, 'button')
esperar_sucesso = partial(esperar_elemento, '#finished')

url = 'https://selenium.dunossauro.live/aula_09_a.html'

driver = Firefox()

wdw = WebDriverWait(driver, 10)

driver.get(url)

wdw.until(esperar_botao, 'Deu ruim')

driver.find_element_by_css_selector('button').click()

wdw.until(
    esperar_sucesso,
    'A mensagem de sucesso não apareceu'
)

sucesso = driver.find_element_by_css_selector('#finished')

assert sucesso.text == 'Carregamento concluído'
