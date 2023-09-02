casaval = float(input('Qual o \033[4;35mvalor\033[m da casa: R$ '))
sal = float(input('Qual é o \033[4;35msalário do comprador\033[m: R$ '))
parcela = int(input('Quantos \033[4;35manos\033[m a casa será \033[4;35mparcelada\033[m: '))
mensalidade = parcela * 12
conta1 = casaval / mensalidade
perce = sal * 0.3
print('O valor de {}cada{} prestação durante os {}{}{} meses de pagamento do Empréstimo será de {}R${:.2f}{}'.format('\033[4;35m','\033[m','\033[4;35m', mensalidade,'\033[m','\033[4;35m',conta1,'\033[m' ))

if conta1 <= perce:
    print('\033[4;30;42mEmpréstimo APROVÁVEL!\033[m')
else:
    print('\033[4;30;41mEmpréstimo NEGADO!\033[m')
    print('\033[4;30;46mReavaliavel\033[m')