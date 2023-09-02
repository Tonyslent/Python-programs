print('\033[33m=\033[m' * 30)
text = '\033[36mSEQUÊNCIA DE FIBONACCI'
print(text.center(30))
print('\033[33m=\033[m' * 30)
x = int(input('Quantos números da sequência você quer: '))
base = 3
pnum = 0
snum = 1
print('{} -> {}'.format(pnum, snum), end='')
while base <= x:
    tnum = pnum + snum
    print(' -> {}'.format(tnum), end='')
    pnum = snum
    snum = tnum
    base += 1
print(' -> \033[34mFIM')
