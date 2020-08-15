from selene.support.shared import browser
from time import sleep

base_url = 'http://selenium.dunossauro.live'

browser.config.base_url = base_url

browser.open('/caixinha')

sleep(3)

browser.open('/keyboard')
