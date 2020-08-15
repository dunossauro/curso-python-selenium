from selene.support.shared import browser
from selene.support.conditions import be, not_
from selene.support import by


browser.open('http://google.com')

browser.s(
    by.name('q')
).should(be.blank).type('live de python')

browser.s(
    by.name('q')
).should(not_.blank).type('100')
