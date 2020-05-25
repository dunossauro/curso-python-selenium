from selenium.webdriver import Firefox

b = Firefox()

url = 'http://selenium.dunossauro.live/aula_06_a.html'

b.get(url)

# usando a atributo type [attr=valor]
# nome = b.find_element_by_css_selector('[type="text"]')
# senha = b.find_element_by_css_selector('[type="password"]')
# btn = b.find_element_by_css_selector('[type="submit"]')

# usando a atributo name [attr=valor]
# nome = b.find_element_by_css_selector('[name="nome"]')
# senha = b.find_element_by_css_selector('[name="senha"]')
# btn = b.find_element_by_css_selector('[name="l0c0"]')

# usando a atributo * [att*=valor]
# nome = b.find_element_by_css_selector('[name*="ome"]')
# senha = b.find_element_by_css_selector('[name*="nha"]')
# btn = b.find_element_by_css_selector('[name*="l0"]')

# usando a atributo | [att|=valor]
# nome = b.find_element_by_css_selector('[name|="nome"]')
# senha = b.find_element_by_css_selector('[name|="senha"]')
# btn = b.find_element_by_css_selector('[name|="l0c0"]')

# usando a atributo ^ [att^=valor]
# nome = b.find_element_by_css_selector('[name^="n"]')
# senha = b.find_element_by_css_selector('[name^="s"]')
# btn = b.find_element_by_css_selector('[name^="l"]')


nome.send_keys('Eduardo')
senha.send_keys('batatinhas123')
btn.click()
