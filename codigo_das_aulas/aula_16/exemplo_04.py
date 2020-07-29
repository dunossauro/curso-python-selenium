from splinter import Browser

b = Browser()
b.visit('http://selenium.dunossauro.live/aula_07.html')
b.fill('nome', 'Fautinho')
b.fill('email', 'faut@o.com')
b.fill('senha', '1234')
# b.find_by_name('btn').click()
b.find_by_value('Enviar!').click()
