from selenium.webdriver import Firefox


b = Firefox()
b.get('http://selenium.dunossauro.live/aula_05_a.html')

elemento_id_a = b.find_element_by_id('a')

print(elemento_id_a.text)
print(elemento_id_a.get_attribute('id'))
