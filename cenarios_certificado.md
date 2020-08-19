## Criação de conta
```feature
Funcionalidade: Criação de conta
  Contexto:
    Dado que esteja na página de "register"

  Cenário: A aplicação deve redirecionar para a página de TODO ao registrar um usuário com sucesso
    Quando registrar minha conta
      | nome      | email         | senha |
      | Beto Cone | beto@cone.com | 123   |
    Então deverá ser redirecionado para a pagina de "todo"

  Cenário: A aplicação deve redirecionar para a página de register ao tentar cadastrar um usuário com e-mail já cadastrado
    Quando registrar minha conta
      | nome      | email         | senha |
      | Beto Cone | beto@cone.com | 123   |
    Dado faça logout
    E que esteja na página de "register"
    Quando registrar minha conta
      | nome      | email         | senha |
      | Beto Cone | beto@cone.com | 123   |
    Então a mensagem de erro deverá ser exibida
      """
      Algo deu errado!
      """

  Cenário: Mensagens do formulário
    Quando coloco o foco no campo de nome
    Então a mensagem de deverá ser exibida
      """
      Lembre-se de colocar um nome falso
      """

    Quando coloco o foco no campo de email
    Então a mensagem de deverá ser exibida
      """
      Se for válido, todo mundo vai saber
      """
    Quando coloco o foco no campo de senha
    Então a mensagem de deverá ser exibida
      """
      Será que é seguro?
      """
```

## Login

```feature
Funcionalidade: Login
  Contexto: Oágina de login
    Dado que esteja na página de "login"

  Cenário: Login com credenciais inválidas
    Quando logar com credenciais inválidas
    Então a mensagem de erro deverá ser exibida
      """
      Email ou senha inválidos!
      """

  Cenário: Login com credenciais válidas
    Quando logar com credenciais válidas
    Então deverá ser redirecionado para a pagina de "todo"

  Cenário: Mensagens do formulário
    Quando coloco o foco no campo de email
    Então a mensagem de deverá ser exibida
      """
      Tá certo?
      """

    Quando coloco o foco no campo de senha
    Então a mensagem de deverá ser exibida
      """
      Não vai errar
      """
```

## Criação de tarefas

```feature
Funcionalidade: Criação de tarefas
  Contexto: Entrar na área logada
    Dado que esteja logado
    E que esteja na página de "todo"

  Cenário: Criar tarefa
    Quando criar tarefa
      | nome   | descrição |
      | Dormir | Pq é bom  |
    Então a tarefa deve estar na pilha "A fazer"
      | nome   | descrição |
      | Dormir | Pq é bom  |

  Cenário: Carregamento automático das TODOS
    Quando criar as tarefas
      | nome           | descrição             | urgente |
      | Liga para Beto | Telefone +15 51515151 | False   |
      | ir no mercado  | Promoção no mercado x | True    |
    E atualizar a página
    Então as tarefas devem estar na pilha "A fazer"
      | nome           | descrição             |
      | Liga para Beto | Telefone +15 51515151 |
      | ir no mercado  | Promoção no mercado x |
    E a tarefa deve estar no topo da pilha "A fazer"
      | nome           | descrição             |
      | ir no mercado  | Promoção no mercado x |

  Cenário: Prioridades de tarefas
      Quando criar as tarefas
        | nome           | descrição               | urgente |
        | Fazer bolo     | não esquecer o fermento | False   |
        | ir no mercado  | Promoção no mercado x   | True    |

      Então a tarefa deve estar no topo da pilha "A fazer"
        | nome           | descrição             |
        | ir no mercado  | Promoção no mercado x |
```

## Movimentação dos cartões

```feature
Funcionalidade: Movimentação de tarefas
  Contexto: Entrar na área logada e registrar tarefas
    Dado que esteja logado
    E que esteja na página de "todo"
    E que as tarefas estejam criadas
      | nome    | descrição         |
      | Dormir  | Pq é bom          |
      | Acordar | Pois é necessário |
      | Comer   | Se não eu morro   |

  Cenário: Mover tarefa para Fazendo
    Quando fazer a tarefa "Dormir"
    Então a tarefa deve estar na pilha "Fazendo"
      | nome   | descrição |
      | Dormir | Pq é bom  |
    E as tarefas devem estar na pilha "A fazer"
      | nome    | descrição |
      | Acordar | Pois é necessário |
      | Comer   | Se não eu morro   |

  Cenário: Mover tarefa para Pronto
    Quando fazer a tarefa "Dormir"
    Então a tarefa deve estar na pilha "Fazendo"
      | nome   | descrição |
      | Dormir | Pq é bom  |
    Quando concluir a tarefa "Dormir"
    Então a tarefa deve estar na pilha "Pronto"
      | nome   | descrição |
      | Dormir | Pq é bom  |

  Cenário: Voltar cartão para A fazer
    Quando fazer a tarefa "Dormir"
    Então a tarefa deve estar na pilha "Fazendo"
      | nome   | descrição |
      | Dormir | Pq é bom  |
    Quando voltar a tarefa "Dormir"
    Então a tarefa deve estar na pilha "A fazer"
      | nome   | descrição |
      | Dormir | Pq é bom  |

  Cenário: Cancelar cartão
    Quando cancelar a tarefa "Dormir"
    Então a tarefa não deve estar na pilha "A fazer"
      | nome   | descrição |
      | Dormir | Pq é bom  |

  Cenário: Cartões devem ser carregados nas colunas corretas
    Quando fazer a tarefa "Dormir"
    E concluir a tarefa "Dormir"
    E fazer a tarefa "Acordar"
    E atualizar a página
    Então a tarefa deve estar na pilha "Fazendo"
      | nome    | descrição         |
      | Acordar | Pois é necessário |
    E a tarefa deve estar na pilha "Pronto"
      | nome   | descrição |
      | Dormir | Pq é bom  |
```
