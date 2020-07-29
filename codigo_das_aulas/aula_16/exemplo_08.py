from splinter import Browser

b = Browser()
b.visit('http://selenium.dunossauro.live/aula_09_a.html')


if b.is_text_not_present('Carregamento concluído'):
    b.find_by_text('Barrinha top').click()


print(
    b.is_text_present(
    'Carregamento concluído',
    wait_time=20
    )
)
