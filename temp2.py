def dias_quentes(temperatura):
    resultados =[]
    for i,dia in enumerate(temperatura):
        media=sum(dia)/len(dia)
        if media>20:
            resultados.append((i,media))
    return resultados


temperatura =[
    [18, 19, 20, 21, 22, 23, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3],
    [21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44]
]

resultado=dias_quentes(temperatura)
for dia,media in resultado:
    print('='*40)
    print(f'dia{dia +1}com maior temp.{media:.2f}°C')
    print('='*40)