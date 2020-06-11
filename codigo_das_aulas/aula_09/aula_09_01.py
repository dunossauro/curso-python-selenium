from selenium.webdriver import Firefox

url = 'https://selenium.dunossauro.live/aula_09_a.html'

f = Firefox()

f.get(url)
f.implicitly_wait(30) # Legal?????

btn = f.find_element_by_css_selector('button')
btn.click()

suecsso = f.find_element_by_css_selector('#finished')
assert suecsso.text == 'Carregamento concluído'

# f.find_element_by_css_selector('Fausto')
