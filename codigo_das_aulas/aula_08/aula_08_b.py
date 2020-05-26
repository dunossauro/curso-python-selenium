from selenium.webdriver import Firefox
from selenium.webdriver.common.action_chains import (
    ActionChains
)
from selenium.webdriver.common.keys import Keys

url = 'https://selenium.dunossauro.live/aula_08_a'
texto = 'Selenium'

browser = Firefox()
browser.get(url)

# hi-level
elemento = browser.find_element_by_name('texto')

# low-level
ac = ActionChains(browser)
ac.move_to_element(elemento)
ac.click(elemento)


def digita_com(key):
    ac.key_down(key)
    for letra in texto:
        ac.key_down(letra)
        ac.key_up(letra)
    ac.key_up(key)

digita_com(Keys.SHIFT)
digita_com(Keys.CAPS)


ac.perform()
