from selenium.webdriver import Firefox
from selenium.webdriver.support.ui import (
    WebDriverWait
)


def esperar_botao(webdriver):
    elements = webdriver.find_elements_by_css_selector(
        'button'
    )
    print('Tentando encontrar "button"')
    return bool(elements) # True ou False


def esperar_sucesso(webdriver):
    elements = webdriver.find_elements_by_css_selector(
        '#finished'
    )
    print('Tentando encontrar "finished"')
    return bool(elements) # True ou False

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
