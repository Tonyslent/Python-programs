cidade = str(input('Qual o \033[1;4;32mnome da cidade\033[m: ')).upper()
cidade1 = cidade.split(' ')
print(f'A cidade de \033[32m{cidade}\033[m da','\033[1;36m','SANTO' in cidade1[0],'\033[m','pra palavra \033[35mSANTO\033[m no começo do nome')