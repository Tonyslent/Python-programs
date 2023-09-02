print('ANO BISSEXTO')
ano = int(input('Qual é o ano que você quer saber se é bissexto: '))
conta1 = ano % 4

if conta1 == 0:
    print(f'O ano de {ano} é bissexto')
else:
    print('O ano não é bissexto')