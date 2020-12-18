from selene.support.shared import browser

base_url = 'http://selenium.dunossauro.live'

browser.config.browser_name = 'chrome'
browser.config.base_url = base_url
browser.config.timeout = 2

browser.open('/caixinha')
