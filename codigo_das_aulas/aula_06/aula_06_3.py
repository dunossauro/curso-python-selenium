from selenium.webdriver import Firefox

b = Firefox()

url = 'http://selenium.dunossauro.live/aula_06_a.html'

b.get(url)

b.find_elements_by_css_selector('div.form-group')

b.find_elements_by_css_selector(
    'div.form-group + br' # br irmão de div class form-group
)[1].get_attribute('id')

# da tag div com a classe form-group pegue o filho com id dentro-nome
b.find_element_by_css_selector('div.form-group > #dentro-nome')
b.find_element_by_css_selector('div.form-group > #dentro-nome')

# do form, pegue todas as tag label existentes
# ignorando a hierarquia (decendente)
b.find_elements_by_css_selector('form label')
