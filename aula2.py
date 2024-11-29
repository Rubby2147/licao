def pode_tirar_ferias(tempo_servico,mes_ferias):
    alta_temporada=['dezembro','janeiro','julho']
    autorizado=False

    if tempo_servico>= 3:
        autorizado= True
    elif tempo_servico < 3 and mes_ferias.lower() not in alta_temporada:
        autorizado= True
    return autorizado

tempo_servico=float(input('há quantos anos trabalha na empresa:'))
mes_ferias=(input('qual mes vai tirar ferias:')) 

if pode_tirar_ferias(tempo_servico,mes_ferias):
    print('pode tirar ferias')
else:
    print('não pode tirar ferias')