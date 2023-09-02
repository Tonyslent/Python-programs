import math

ang = float(input('\033[1;4;40mDigite aqui qualquer angulo:\033[m '))
cos = math.cos(math.radians(ang))
sen = math.sin(math.radians(ang))
tang = math.tan(math.radians(ang))

print('O valor do \033[31mSeno\033[m, \033[32mCosseno\033[m e \033[36mTangente\033[m nessa seguinte ordem é: \033[31m{:.2f}\033[m, \033[32m{:.2f}\033[m e \033[36m{:.2f}\033[m'.format(sen, cos, tang))