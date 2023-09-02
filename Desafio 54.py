from datetime import date
contadormaior = 0
contadormenor = 0
anobase = date.today().year
for idade in range(1, 8):
    ano = int(input('Qual o ano de nascimento da {}ª pessoa: '.format(idade)))
    data = anobase - ano
    if data >= 21:
        contadormaior += 1
    elif data < 21:
        contadormenor += 1
print('Das 7 pessoas entrevistadas, {} são maiores de idade, e {} delas ainda não'.format(contadormaior, contadormenor))
