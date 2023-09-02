text = 'SOMA DE VARIOS VALORES'
print(text.center(40, '='))
print('Número de parada = 999')
x = int(input('Digite um número: '))
somatoria = 0
acumulador = 0
while x < 999:
    somatoria += x
    x = int(input('Digite um número: '))
    acumulador += 1
print('A quantidade de números digitados foi de {} e a soma de todos os valores inseridos é {}'.format(acumulador, somatoria))