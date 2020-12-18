from selene import Browser, Config
from selenium.webdriver import Remote

base_url = 'http://selenium.dunossauro.live'

browser = Browser(
    Config(
        driver=Remote(
            desired_capabilities={'browserName': 'firefox'}
        ),
        base_url=base_url,
    )
)

browser.open('/caixinha')
