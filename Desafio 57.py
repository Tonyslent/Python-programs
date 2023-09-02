sexo = str(input('Qual o seu sexo \033[1;32m[M/F]\033[m : ').upper())
while sexo not in 'MmFf':
    sexo = str(input('Invalido, digite novamente\nQual o seu sexo \033[1;32m[M/F]\033[m : ').upper())
if sexo == 'M':
    print('Sexo masculino registrado')
if sexo == 'F':
    print('Sexo feminino registrado')