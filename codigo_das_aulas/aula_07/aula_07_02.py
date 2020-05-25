"""
1. Checar se a mudança ocorre no span (focus, blur) - OK
2. Checar se a mudança ocorre no p (change) - OK
"""
from selenium.webdriver import Firefox
from selenium.webdriver.support.events import (
    AbstractEventListener,
    EventFiringWebDriver
)


class Escuta(AbstractEventListener):
    def after_navigate_to(self, url, webdriver):
        print(f'Indo para {url}')

    def after_navigate_back(self, webdriver):
        print('voltando para página anterior')


    def before_click(self, elemento, webdriver):
        if elemento.tag_name == 'input':
            print(webdriver.find_element_by_tag_name('span').text)
        print(f'antes do click no {elemento.tag_name}')

    def after_click(self, elemento, webdriver):
        if elemento.tag_name == 'input':
            print(webdriver.find_element_by_tag_name('span').text)
        print(f'depois do click no {elemento.tag_name}')


browser = Firefox()

rapi_browser = EventFiringWebDriver(browser, Escuta())

rapi_browser.get('https://selenium.dunossauro.live/aula_07_d')

input_de_texto = rapi_browser.find_element_by_tag_name('input')
span = rapi_browser.find_element_by_tag_name('span')
p = rapi_browser.find_element_by_tag_name('p')

input_de_texto.click()
span.click()

rapi_browser.get('https://selenium.dunossauro.live/aula_07_c')

rapi_browser.back()

browser.quit()
