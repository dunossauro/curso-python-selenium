from selene.support.shared import browser
from selene import by

base_url = 'http://selenium.dunossauro.live'

browser.config.base_url = base_url

browser.open('/aula_07')
browser.element(by.css('input')).type('Duduzinho da massa')
browser.ss(by.css('input'))
