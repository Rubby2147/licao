vendas =[('produtos a',10),('produtos b',20),('produtos c',30)]

total_de_vendas={}

contagen={}

for produto in vendas:
    if produto in total_de_vendas:
        total_de_vendas[produto]
        contagen[produto] +=1
    else:
        total_de_vendas[produto] = vendas
        contagen = 1

print('relatorio de vendas:')

for produtos in total_de_vendas:
    media= total_de_vendas[produto]/contagen[produto]
    print(f'{produto} ,total de vendas= {total_de_vendas[produto]}, media de vendas ={media:2f}')