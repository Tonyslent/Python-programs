frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
reverso = ''
for letras in range(len(junto) - 1, -1, -1):
    reverso += junto[letras]
print('O inverso de {} é {}'.format(frase, reverso))
if reverso == junto:
    print('\033[32mA frase é um palíndromo!')
else:
    print('\033[31mA frase não é um palíndromo!')