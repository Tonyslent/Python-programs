print('\033[1;30;41mOFERTA RELÂMPAGO: Compre 2 camisas da loja e tenha 5% de desconto!!!\033[m')
x = float(input('\033[1;35mSISTEMA\033[m: Qual o preço da roupa a ser comprada: '))

desconto = 0.05
valor = x * desconto
valorf = x - valor

print('\033[4;36mR${:.2f}'.format(valorf))