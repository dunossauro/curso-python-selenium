from selenium.webdriver import Firefox
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.expected_conditions import (
    new_window_is_opened,
    number_of_windows_to_be
)


browser = Firefox()
wdw = WebDriverWait(browser, 60)

browser.get('http://selenium.dunossauro.live/aula_11_b')

browser.find_element_by_id('popupd')

# wdw.until(
#     new_window_is_opened(browser.window_handles)
# )

wdw.until(
    number_of_windows_to_be(2)
)

print('abriu')
