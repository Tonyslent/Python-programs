from time import sleep
print('\033[36m--' * 19)
print('TABUADA'.center(38))
print('--' * 19)
while True:
    x = int(input('\033[mDigite qual \033[33mtabuada\033[m você deseja: '))
    sleep(0.5)
    if x < 0:
        break
    print('\033[36m--\033[m' * 19)
    for tabuada in range(1, 11):
        numero = x * tabuada
        print(f'{x} \033[35mx\033[m {tabuada} \033[35m=\033[m {numero}')
    print('\033[36m--\033[m' * 19)
print('\033[36m--\033[m' * 19)
print('\033[31mTABUADA ENCERRADA'.center(42))
print('\033[36m--\033[m' * 19)

