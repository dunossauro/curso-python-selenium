from abc import ABC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from todo_project.page_objects import PageElement


class Todo(PageElement):
    name = (By.ID, 'todo-name')
    description = (By.ID, 'todo-desc')
    urgent = (By.ID, 'todo-next')
    submit = (By.ID, 'todo-submit')

    def create_todo(self, name, description, urgent=False):
        self.webdriver.find_element(*self.name).send_keys(name)
        self.webdriver.find_element(*self.description).send_keys(description)
        if urgent:
            self.webdriver.find_element(*self.urgent).click()
        self.webdriver.find_element(*self.submit).click()


class CardContainer(PageElement, ABC):
    @property
    def todos(self):
        cards = self.find_elements(self.card)
        # return [Card(card) for card in cards]
        po_cards = []
        for card in cards:
            po_cards.append(Card(card))

        return po_cards


class AFazer(CardContainer):
    fieldset = (By.CSS_SELECTOR, 'div.body_a fieldset')
    card = (By.CLASS_NAME, 'terminal-card')


class Fazendo(CardContainer):
    fieldset = (By.CSS_SELECTOR, 'div.body_b fieldset')
    card = (By.CLASS_NAME, 'terminal-card')


class Pronto(CardContainer):
    fieldset = (By.CSS_SELECTOR, 'div.body_c fieldset')
    card = (By.CLASS_NAME, 'terminal-card')


class Card:
    def __init__(self, selenium_object):
        self.selenium_object = selenium_object
        self.name = By.CSS_SELECTOR, 'header.name'
        self.description = By.CSS_SELECTOR, 'div.description'
        self._do = By.CSS_SELECTOR, 'button.do'
        self._cancel = By.CSS_SELECTOR, 'button.cancel'
        self._load()

    def do(self):
        self.selenium_object.find_element(*self._do).click()

    def cancel(self):
        try:
            self.selenium_object.find_element(*self._cancel).click()
        except NoSuchElementException:
            print('Elemento não tem cancelar')

    def _load(self):
        self.name = self.selenium_object.find_element(
            *self.name
        ).text
        self.description = self.selenium_object.find_element(
            *self.description
        ).text

    def __repr__(self):
        return f'Card(name="{self.name}", description="{self.description}")'
