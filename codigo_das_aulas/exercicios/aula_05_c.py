from selenium.webdriver import Firefox


b = Firefox()
b.get('http://selenium.dunossauro.live/aula_05_c.html')

elementos = b.find_elements_by_tag_name('p')

for elemeneto in elementos:
    if 'fundo' in elemeneto.get_attribute('class'):
        print(elemeneto.text)
