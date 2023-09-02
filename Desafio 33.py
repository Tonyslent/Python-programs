print('MENOR E MAIOR')
num1 = int(input('Qual é o primeiro número: '))
num2 = int(input('Qual é o segundo: '))
num3 = int(input('Qual é o ultimo: '))
maior = num1
menor = num1
#teste de maior
if num2 > num1 and num2 > num3:
    maior = num2
if num3 > num1 and num3 > num2:
    maior = num3
#teste de menor
if num2 < num1 and num2 < num3:
    menor = num2
if num3 < num1 and num3 < num2:
    menor = num3
print(f'O maior número é {maior}')
print(f'O menor número  é {menor}')