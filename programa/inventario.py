inventario ={}

while True:
    acao=input('digite:adicionar,remover,exibir ou sair:')

    if acao== 'adicionar':
        produto = input('digite produto')
        preco=float(input('digite preco:'))
        inventario[produto]=preco
        print(f'O produto{produto} foi adicionado ao inventario, preço R${preco}')

    elif acao=='remover':
        produto=input('digite o produto para remover')
        if produto in inventario:
            del inventario[produto]
            print('produto foi removido')
        else:
            print('produto não encrontado')

    elif acao== 'exibir':
        print(inventario)
        for produto,preco in inventario.items():
            print(f'protudo{produto}: r$ {preco}')

    elif acao=='sair':
        break
    else:
        print('opção invalida, tente novamente')