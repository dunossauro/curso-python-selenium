from selenium.webdriver import Firefox
from selenium.webdriver.common.action_chains import (
    ActionChains
)
from selenium.webdriver.common.keys import Keys

url = 'https://selenium.dunossauro.live/caixinha'

browser = Firefox()
browser.get(url)

caixa = browser.find_element_by_id('caixa')
span = browser.find_element_by_tag_name('span')

ac = ActionChains(browser)


def caixinha_colorida(key1, key2=None):
    ac.pause(1)
    ac.key_down(key1)
    if key2:
        ac.key_down(key2)
    ac.move_to_element(caixa)
    ac.click()
    ac.double_click()
    ac.move_to_element(span)
    ac.key_up(key1)
    if key2:
        ac.key_up(key2)


ac.drag_and_drop(elemto_a, elemento_b)

ac.click_and_hold(elemto_a)
ac.move_to_element(elemto_b)
ac.release(elemto_b)

caixinha_colorida(Keys.SHIFT)
caixinha_colorida(Keys.CONTROL)
caixinha_colorida(Keys.SHIFT, Keys.CONTROL)

ac.move_to_element(caixa)
ac.context_click()
ac.perform()
