from selene.support.shared import browser
from selene.support.conditions import be
from selene.support.conditions import have


browser.open(
    'http://selenium.dunossauro.live/aula_07'
)

label = browser.element(
    '[for="nome"]'
)

label.should(have.text('nome'))


browser.all(
    'input'
).should(have.size(4)).first.type('Duduzin')


label.should(have.text('Não vale mentir o nome'))
