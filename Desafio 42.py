print('triangulo verdadeiro ou falso'.upper())
l1 = int(input('Qual o tamanho da primeira linha: '))
l2 = int(input('Qual é o tamanho do segundo: '))
l3 = int(input('Qual é o ultimo tamanho: '))
if l1 < (l2 + l3) and l2 < (l1 + l3) and l3 < (l1 + l2):
    print('Com essas medidas você pode formar um triangulo ', end='')
    if l1 == l2 == l3:
        print('\033[1;32mEQUILATERO!')
    elif l1 != l2 != l3 != l1:
        print('\033[1;32mESCALENO!')
    else:
        print('\033[1;32mISÓCELES!')
else:
    print('Com essas medidas você não pode criar um triangulo!')