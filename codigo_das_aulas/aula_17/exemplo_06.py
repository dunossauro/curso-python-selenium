from selene.support.shared import browser

base_url = 'http://selenium.dunossauro.live'

browser.config.base_url = base_url

browser.open('/aula_07')
browser.s('input').type('Duduzinho da massa')
browser.ss('input')
