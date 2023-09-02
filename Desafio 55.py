pesomaior = 0
pesomenor = 0
for pesog in range(1, 6):
    peso = float(input('Qual o peso da {}ª pessoa: '.format(pesog)))
    if pesog == 1:
        pesomaior = peso
        pesomenor = peso
    else:
        if peso > pesomaior:
            pesomaior = peso
        if peso < pesomenor:
            pesomenor = peso

print('O \033[33mmaior\033[m peso registrado foi de {} KG'.format(pesomaior))
print('O \033[33mmenor\033[m peso registrado foi de {} KG'.format(pesomenor))
