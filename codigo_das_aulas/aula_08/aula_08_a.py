from selenium.webdriver import Firefox


url = 'https://selenium.dunossauro.live/keyboard'

browser = Firefox()

browser.get(url)

html = browser.find_element_by_tag_name('html')

html.send_keys('selenium')
