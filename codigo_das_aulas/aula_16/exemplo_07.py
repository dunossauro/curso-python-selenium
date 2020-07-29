from splinter import Browser

b = Browser()
b.visit('http://selenium.dunossauro.live/caixinha.html')

caixa = b.find_by_id('caixa')

caixa.click()

# AC
caixa.mouse_over()
caixa.double_click()
caixa.right_click()
# caixa.mouse_out()
