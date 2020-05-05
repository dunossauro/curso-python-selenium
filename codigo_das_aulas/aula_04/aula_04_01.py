from selenium.webdriver import Firefox

browser = Firefox()

browser.get('http://selenium.dunossauro.live/aula_04_a.html')

lista_n_ordenada = browser.find_element_by_tag_name('ul')  # 1

lis = lista_n_ordenada.find_elements_by_tag_name('li')  # 2

lis[0].find_element_by_tag_name('a').text  # 3

"""
1. buscamos `ul`
2. buscamos todos `li`
3. No primeiro `li`, buscamos `a` e pegamos o seu texto

ul
    li
        a
            texto
    li
        a
            texto

"""
