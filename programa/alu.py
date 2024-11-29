quantidade_alunos= int(input('digite a quantidade de alunos:'))

sum_notas = 0

for i in range(quantidade_alunos):
    notas=float(input(f'digite notas {i+1}:'))
    sum_notas+=notas

media= sum_notas/quantidade_alunos

print(f'media:{media}')