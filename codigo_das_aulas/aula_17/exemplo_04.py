from selene.support.shared import browser

base_url = 'http://google.com'

browser.config.base_url = base_url

browser.open('')
# browser.element('input[name="q"]').type('Live de python')
browser.element(
    '//*[@name="q"]'
).type('Live de python').press_enter()
