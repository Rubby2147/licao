temperatura = [
    [22,25,28,32],
    [20,23,26,30],
    [18,22,25,29]
]

matriz_transposta = list(zip(*temperatura))

print('matriz transpost')
for linha in matriz_transposta:
    print(linha)