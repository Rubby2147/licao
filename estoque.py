def Vender(estoque,produtos,quantidade):
    if estoque[produtos-1]>=quantidade:
        estoque[produtos-1]-=quantidade

    else:
        print('estoque insuficiente')

def Adicioinar(estoque,produtos,quantidade):  
        estoque[produtos-1]+=quantidade
    
def Exibir_estoque(estoque):
    for i,qtde in enumerate(estoque,start=1):
        print(f'produtos{i}: {qtde} unidades')

estoque =[20, 15, 10, 30, 5]

Vender(estoque,1,3)
Vender(estoque,4,2)
Adicioinar(estoque,5,10)
Exibir_estoque(estoque)