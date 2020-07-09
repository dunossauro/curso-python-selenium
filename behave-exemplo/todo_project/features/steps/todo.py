from json import loads
from behave import given, when, then
from todo_project.pages.pages import PageTodo


@given('que eu esteja na página {page}')
def go_to_page(context, page):
    context.page = PageTodo(
        context.browser,
        'http://selenium.dunossauro.live/todo_list.html'
    )

    context.page.open()

@when('criar um todo')
def create_todo(context):
    texto_do_step = loads(context.text)

    context.page.todo.create_todo(
        name=texto_do_step['nome'],
        description=texto_do_step['descrição']

    )


@when('criar os seguintes todos')
def create_many_todos(context):
    for linha in context.table.rows:
        linha_convertida = dict(linha.items())

        urgent = False

        if linha_convertida.get('urgente'):
            urgent = True if linha_convertida['urgente'] == 'sim' else False

        context.page.todo.create_todo(
            name=linha_convertida['nome'],
            description=linha_convertida['descrição'],
            urgent=urgent
        )


@then('o todo deve estar na pilha "{elemento}"')
def check_todo(context, elemento):
    elemento = elemento.lower().replace(' ', '_')

    page_element = getattr(context.page, elemento)

    assert 1 == len(page_element.todos)


@then('o cartão deve estar na pilha "{elemento}"')
def check_todo(context, elemento):
    elemento = elemento.lower().replace(' ', '_')

    page_element = getattr(context.page, elemento)

    table_value = dict(context.table.rows[0].items())

    page_element.todos[0].name == table_value['nome']


@then('o cartão deve estar no topo da pilha "{elemento}"')
def check_todo(context, elemento):
    elemento = elemento.lower().replace(' ', '_')

    page_element = getattr(context.page, elemento)

    table_value = dict(context.table.rows[0].items())

    page_element.todos[0].name == table_value['nome']
