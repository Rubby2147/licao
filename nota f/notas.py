list=[]
for i in range(4):
    num=int(input('qual o numero:'))
    if num <0 or num> 10:
        print ('numero invalido')
    else:
        list.append(num)
media=(sum(list))/4
sorted(list)
print(f'a media é:{media}, as notas são:{list}')