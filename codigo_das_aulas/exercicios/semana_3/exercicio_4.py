from selenium.webdriver import Firefox
from time import sleep
from urllib.parse import urlparse, parse_qsl


url = 'https://selenium.dunossauro.live/exercicio_04.html'

f = Firefox()

f.get(url)

sleep(3)

form = {
    'nome': f.find_element_by_name('nome'),
    'email': f.find_element_by_name('email'),
    'senha': f.find_element_by_name('senha'),
    'telefone': f.find_element_by_name('telefone'),
    'btn': f.find_element_by_name('btn')
}

form['nome'].send_keys('eduardo')
form['email'].send_keys('eduardo@eduardo.com')
form['senha'].send_keys('1q2w3e')
form['telefone'].send_keys('987654321')
form['btn'].click()


# -------------- parte 2
sleep(2)
dict_text_area = eval(f.find_element_by_tag_name('textarea').text)

dict_text_url = dict(parse_qsl(urlparse(f.current_url).query))

dict_text_url.pop('btn')


assert dict_text_area == dict_text_url
