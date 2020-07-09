Funcionalidade: Todo List

  Cenário: Criar um cartão de todo
    Dado que eu esteja na página "todo"
    Quando criar um todo
      """
        {
          "nome": "Dormir",
          "descrição": "é bom"
        }
      """
    Então o todo deve estar na pilha "A fazer"

  Cenário: Criar dois cartões de todo
    Dado que eu esteja na página "todo"
    Quando criar os seguintes todos
      | nome   | descrição   |
      | Dormir | é bom       |
      | Comer  | Ao meio dia |

    Então o cartão deve estar na pilha "A fazer"
      | nome   | descrição   |
      | Dormir | é bom       |

  Cenário: Criar cartão urgente
    Dado que eu esteja na página "todo"
    Quando criar os seguintes todos
      | nome   | descrição   | urgente |
      | dormir | é bom       | não     |
      | comer  | ao meio dia | sim     |

    Então o cartão deve estar no topo da pilha "A fazer"
      | nome   | descrição   |
      | comer  | ao meio dia |
