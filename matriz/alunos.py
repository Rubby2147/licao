dados=[]

quant=int(input('quantas pessoas:'))

for i in range(quant):
    print(f'cadastro de dados:{i+1}')
    nome=input('digite o nome:')
    turma=input('digite o nome da turma:')
    escola=input('digite o nome da escola:')
    print('='*50)
    dados.append([nome,turma,escola])
print('matrz de dados:')
for registro in dados:
    print(dados)
