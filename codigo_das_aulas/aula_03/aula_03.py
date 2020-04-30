from selenium.webdriver import Firefox
from time import sleep

url = 'https://curso-python-selenium.netlify.app/aula_03.html'

navegador = Firefox()

navegador.get(url)

sleep(1)

a = navegador.find_element_by_tag_name('a')


for click in range(10):
    ps = navegador.find_elements_by_tag_name('p')
    a.click()
    print(f'Valor do ultimo p: {ps[-1].text} valor do click: {click}')

    print(f'Os valors são iguais {ps[-1].text == str(click)}')


navegador.quit()
