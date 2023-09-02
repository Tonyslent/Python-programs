print('PASSAGEM 0,50 CENTAVOS POR KM')
km = int(input('Qual a distancia exata até seu destino em QUILOMETROS:\nOBS: apartir de 200km de viagem, o preço da passagem vai ser 45 centavos por quilometro '))
preco = km * 0.5
preco2 = km * 0.45
if km <= 200:
    print('O preço da sua viagem vai ser de {:.2f} reais'.format(preco))
if km > 200:
    print('O preço da sua viagem vai ser de {:.2f} reais'.format(preco2))