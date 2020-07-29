from splinter import Browser

b = Browser()
b.visit('http://selenium.dunossauro.live/aula_07.html')
b.find_by_css('.terminal-menu')\
 .links\
 .find_by_partial_href('Youtube')\
 .click()
