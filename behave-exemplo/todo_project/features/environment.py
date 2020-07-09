from selenium.webdriver import Firefox, Chrome
from ipdb import spost_mortem


def before_all(context):
    browser = context.config.userdata.get('browser')

    browsers = {
        'chrome': Chrome,
        'firefox': Firefox
    }
    context.browser = browsers[browser]()


def after_all(context):
    context.browser.quit()


def after_step(context, step):

    if context.config.userdata.getbool("debug") and step.status == 'failed':
        spost_mortem(step.exc_traceback)
