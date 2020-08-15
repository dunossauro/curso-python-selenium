from selene.support.shared import browser
from selene.support.conditions import be
from selene.support.conditions import have


browser.open('http://google.com')

browser.element(
    'input[name="q"]'
).should(be.blank).type('Envydust').press_enter()
