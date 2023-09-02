from time import sleep
print('\033[1;4;35mSEQUÊNCIA NUMERIA DE PARES\033[m')
sleep(2)
for c in range(0, 51, +2):
    print(c)
    sleep(0.5)
print('\033[1;4;35mFIM\033[m')