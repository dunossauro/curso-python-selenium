from selenium.webdriver import Firefox


def find_by_text(browser, tag, text):
    """Encontrar o elemento com o texto `text`.

    Argumentos:
        - browser = Instancia do browser [firefox, chrome, ...]
        - texto = conteúdo que deve estar na tag
        - tag = tag onde o texto será procurado
    """
    elementos = browser.find_elements_by_tag_name(tag)  # lista

    for elemento in elementos:
        if elemento.text == text:
            return elemento


def find_by_href(browser, link):
    """Encontrar o elemento `a` com o link `link`.

    Argumentos:
        - browser = Instancia do browser [firefox, chrome, ...]
        - link = link que será procurado em todos as tags `a`
    """
    elementos = browser.find_elements_by_tag_name('a')

    for elemento in elementos:
        if link in elemento.get_attribute('href'):
            return elemento


browser = Firefox()

browser.get('http://selenium.dunossauro.live/aula_04_a.html')

# elemento_ddg = find_by_text(browser, 'a', 'DuckDuckGo')

elemento_ddg = find_by_href(browser, 'ddg')
