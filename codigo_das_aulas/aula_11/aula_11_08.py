from selenium.webdriver import Firefox

browser = Firefox()

browser.get('http://selenium.dunossauro.live/aula_11_c')

print(f'Janelas: {len(browser.window_handles)}')

browser.find_element_by_tag_name('button').click()

print(f'Janelas: {len(browser.window_handles)}')
