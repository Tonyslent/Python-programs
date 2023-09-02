print('triangulo verdadeiro ou falso'.upper())
l1 = int(input('Qual o tamanho da primeira linha: '))
l2 = int(input('Qual é o tamanho do segundo: '))
l3 = int(input('Qual é o ultimo tamanho: '))
if l1 < (l2 + l3) and l2 < (l1 + l3) and l3 < (l1 + l2):
    print('Com essas medidas você pode formar um triangulo!')
else:
    print('Com essa medida você não pode fazer um triangulo!')