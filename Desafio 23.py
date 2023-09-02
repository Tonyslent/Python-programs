num = int(input('\033[1;40mdigite aqui um número de 0 a 9999:\033[m '))

un = num // 1 % 10
deze = num // 10 % 10
cen = num // 100 % 10
mil = num // 1000 % 10

print('O número {} separado em casas é:\n\033[31mUnidade\033[m: {}\n\033[32mDezena\033[m: {}\n\033[33mCentena\033[m: {}\n\033[34mMilhar\033[m: {}'.format(num, un, deze, cen, mil))
