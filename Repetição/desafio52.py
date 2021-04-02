num = int(input('Informe um número : '))
total = 0
for c in range(1,num + 1):
    if num % c == 0:
        print('\033[33m', end= '')
        total += 1 #O resto da divisão + 1, para ele verificar o número primo
    else:
        print('\033[31m', end= ' ')
    print('{}'.format(c), end= ' ')
print('\n\033[mO número {}, foi dividido {} vezes '.format(num,total))
if total == 2:
    print('É por isso que ele é primo !')
else:
    print('Por isso ele não é primo !')