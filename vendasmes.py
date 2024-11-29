import numpy as np 
vendas=np.array([120,130,140,150,160,170,160,150,140,130,120,110])

total_vendas= vendas.sum()
media= vendas.mean() 
maior = vendas.argmax()+1

print('relatorio de vendas')
print(f'total de vendas:{total_vendas}')
print(f'media de vendas:{media}')
print(f'mes com maior venda:{maior}')