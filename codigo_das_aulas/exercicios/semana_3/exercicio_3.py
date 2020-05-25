from selenium.webdriver import Firefox
from time import sleep
from urllib.parse import urlparse


url = 'https://selenium.dunossauro.live/exercicio_03.html'


def find_a_by_attr(browser, attr, val):
    elementos = browser.find_elements_by_tag_name('a')
    for elemento in elementos:
        if elemento.get_attribute(attr) == val:
            return elemento


def find_a_by_content(browser, content):
    elementos = browser.find_elements_by_tag_name('a')
    for elemento in elementos:
        if elemento.text == content:
            return elemento


browser = Firefox()
browser.get(url)

# pagina 0
sleep(3)
main = browser.find_element_by_tag_name('main')
main.find_element_by_tag_name('a').click()

# pagina 1
sleep(3)
main = browser.find_element_by_tag_name('main')
find_a_by_attr(main, 'attr', 'errado').click()


# pagina 2
sleep(40)
main = browser.find_element_by_tag_name('main')
titulo = browser.title
find_a_by_content(main, browser.title).click()


# pagina 3
sleep(3)
main = browser.find_element_by_tag_name('main')
parsed_url = urlparse(browser.current_url)
find_a_by_content(main, parsed_url.path[1:]).click()


# pagina 4
sleep(3)
browser.refresh()
