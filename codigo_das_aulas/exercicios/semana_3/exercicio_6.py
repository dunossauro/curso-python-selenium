from selenium.webdriver import Firefox
from time import sleep


url = 'https://selenium.dunossauro.live/exercicio_06.html'

f = Firefox()

f.get(url)


def preenche_form(browser, form, nome, senha):
    inputs_form = {
        'nome': browser.find_element_by_css_selector(
            f'.form-{form} [name="nome"]'
        ),
        'senha': browser.find_element_by_css_selector(
            f'.form-{form} [name="senha"]'
        ),
        'enviar': browser.find_element_by_css_selector(
            f'.form-{form} [type="submit"]'
        ),
    }
    inputs_form['nome'].send_keys(nome)
    inputs_form['senha'].send_keys(senha)
    inputs_form['enviar'].click()


for n in range(6):
    sleep(3)
    form = f.find_element_by_css_selector('span').text
    preenche_form(f, form, f'eduardo{n}', f'1234{n}')
