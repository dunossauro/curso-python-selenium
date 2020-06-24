from selenium.webdriver import Chrome

browser = Chrome()

browser.get('http://selenium.dunossauro.live/aula_11_b')

browser.current_window_handle  # id da janela atual
wids = browser.window_handles  # ids de todas as janelas


def find_window(url: str):
    wids = browser.window_handles
    for window in wids:
        browser.switch_to.window(window)
        if url in browser.current_url:
            break

find_window('duckduckgo')
