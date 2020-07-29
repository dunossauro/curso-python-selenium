from splinter import Browser

b = Browser()
b.visit('http://selenium.dunossauro.live/aula_07.html')
b.find_by_css('input')[3].click()  # slice
# lazy
