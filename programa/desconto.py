while True:
    num=int(input('quantas roupas compro:'))
    cost=int(input('quanto custa a peça:'))
    if 0<num<=5:
        print('o custo sera:',(cost*num))
        print('desconto de:',(0))
    elif num>5 and num<=10:
        print('o custo sera:',(cost-cost*0.1)*num)
        print('desconto de:',(cost*0.1)*num)
    elif num>10:
        print('o custo sera:',(cost-cost*0.2)*num)
        print('desconto de:',(cost*0.2)*num)
    else:
        print('valor invalido')