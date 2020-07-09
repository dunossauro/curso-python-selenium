from todo_project.page_objects import Page
from .elements import AFazer, Fazendo, Pronto, Todo


class PageTodo(Page):
    a_fazer = AFazer()
    fazendo = Fazendo()
    pronto = Pronto()
    todo = Todo()
