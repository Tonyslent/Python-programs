from time import sleep
fogos = '\033[1;31m FOGOS DE ANO NOVO!!! \033[m'
traco = '\033[1;31m-'
print(fogos.center(50, '-'))
print('CONTAGEM REGRESSIVA')
for contagem in range(10, 0, -1):
    print(contagem)
    sleep(1)
print('\033[1;32mJÁ!!!')