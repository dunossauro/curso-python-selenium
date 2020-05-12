from selenium.webdriver import Firefox


url = 'http://selenium.dunossauro.live/aula_05_c.html'

firefox = Firefox()

firefox.get(url)


def melhor_filme(browser, filme, email, telefone):
    """Preenche o formulário do melhor filme de 2020."""
    browser.find_element_by_name('filme').send_keys(filme)
    browser.find_element_by_name('email').send_keys(email)
    browser.find_element_by_name('telefone').send_keys(telefone)
    browser.find_element_by_name('enviar').click()


melhor_filme(
    firefox,
    'Parasita',
    'dudu@du.edu',
    '(019)987654321'
)

firefox.quit()
