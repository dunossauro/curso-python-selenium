from selenium.webdriver import Firefox

browser = Firefox()

browser.get('http://selenium.dunossauro.live/aula_11_c')

browser.execute_script('window.open("")')

browser.switch_to.window(
    browser.window_handles[-1]
)

browser.get('http://ddg.gg')
