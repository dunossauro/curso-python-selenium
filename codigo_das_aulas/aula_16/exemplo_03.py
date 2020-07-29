from splinter import Browser
# from selenium.webdriver import Firefox

b = Browser()
# b = Firefox()
b.visit('http://google.com')
# b.get('http://google.com')
b.find_by_name('q').type('Live de Python')
# b.find_element_by_name('q').send_keys('Live de Python')
b.find_by_name('btnK').click()
# b.find_element_by_name('btnK').click()
