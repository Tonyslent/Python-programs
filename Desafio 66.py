contador = soma = 0
while True:
    x = int(input('Digite um número [\033[32m999 para o programa\033[m]: '))
    if x == 999:
        break
    contador += 1
    soma += x
print(f'A soma dos \033[35m{contador}\033[m números é \033[35m{soma}\033[m')
