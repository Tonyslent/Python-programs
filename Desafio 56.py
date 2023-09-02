sexom = ''
sexof = ''
idadem = 0
idadehmv = 0
idadef = 0
mulher_20 = 0
nomem = ''
media = 0
x = int(input('Quantas \033[1;35mpessoas\033[m você quer registrar: '))
for pesquisa in range(1, x + 1):
    x = ' {}ª pessoa '.format(pesquisa).upper()
    x1 = x.center(20, '=')
    print(x1)
    nome = str(input('Qual o seu \033[1;34mnome\033[m: ').upper())
    sexo = str(input('Qual o seu \033[1;31msexo\033[m [M/F]: ').upper())
    if sexo == 'M':
        sexom = sexo
    elif sexo == 'F':
        sexof = sexo
    idade = int(input('Qual a sua \033[1;33midade\033[m: ').upper())
    if sexo == 'M':
        idadem += idade
        if sexo == 'M' and pesquisa == 1:
            idadehmv = idade
            nomem = nome
        elif sexo == 'M' and pesquisa == 2 or 3 or 4:
            if idadehmv > idade:
                idadehmv = idadehmv
            elif idadehmv < idade:
                idadehmv = idade
                nomem = nome
    elif sexo == 'F':
        idadef += idade
    if sexo == 'F' and idade < 20:
        mulher_20 += 1
    if pesquisa == 4:
        print('=' * 20)
media = (idadef + idadem) / 4
print('A idade media do grupo é de \033[1;35m{}\033[m anos'.format(media))
print('O homem mais velho do grupo tem \033[1;35m{}\033[m anos e seu nome é \033[1;35m{}\033[m'.format(idadehmv, nomem))
print('Ao todo, \033[1;35m{}\033[m mulher(es) tem \033[1;35mmenos\033[m de 20 anos de idade'.format(mulher_20))
