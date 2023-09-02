#variaveis e historia
print('\033[1;35;40m=========== TONYSTORE ============\033[m')
x = float(input('Qual o valor \033[34mtotal\033[m das compras: R$'))
y = int(1)
print('''\033[1;35;40m===== CONDIÇÕES DE PAGAMENTO =====\033[m
\033[1;35m[ 1 ]\033[m - \033[1;33mÀ VISTA\033[m - \033[1;36mDINHEIRO\033[m - \033[1;32m10% DE DESCONTO\033[m
\033[1;35m[ 2 ]\033[m - \033[1;33mÀ VISTA\033[m - \033[1;36mCARTÃO\033[m - \033[1;32m5% DE DESCONTO\033[m
\033[1;35m[ 3 ]\033[m - \033[1;33mPARCELADO\033[m - \033[1;36mCARTÃO\033[m - \033[1;32m2X\033[m - \033[1;32mSEM JUROS\033[m
\033[1;35m[ 4 ]\033[m - \033[1;33mPARCELADO\033[m - \033[1;36mCARTÃO\033[m - \033[1;32m3X OU MAIS\033[m - \033[1;32m20% JUROS\033[m''')
condi = int(input('Qual será a forma de \033[34mPagamento\033[m:'))
if condi == 4:
    y = int(input('Quantas \033[1;33mparcelas\033[m: '))
#calculos
avista1 = (x * 0.1)
avista1_2 = x - avista1
avista2 = (x * 0.05)
avista2_2 = x - avista2
parcela1 = x / 2
parcela2 = (x * 0.2)
parcela2_2 = x + parcela2
parcela2_3 = parcela2_2 / y
#comandos
if condi == 1:
    print('O preço a se pagar em dinheiro vai ser de \033[1;32mR${:.2f}\033[m com o desconto aplicado'.format(avista1_2))
elif condi == 2:
    print('O preço a se pagar no cartão vai ser de \033[1;32mR${:.2f}\033[m com o desconto aplicado'.format(avista2_2))
elif condi == 3:
    print('''Sua compra será \033[1;33mparcelada\033[m em \033[1;36m2X sem juros\033[m
Cada \033[1;33mparcela\033[m vai custar \033[1;32mR${:.2f}\033[m'''.format(parcela1))
elif condi == 4:
    print('''Sua compra de \033[1;32mR${:.2f}\033[m vai ser \033[1;33mparcelada\033[m em \033[1;33m{}x\033[m de \033[1;32mR${:.2f}\033[m 
e o preço total \033[1;32mcom juros\033[m será de \033[1;32mR${:.2f}\033[m'''.format(x, y, parcela2_3, parcela2_2))