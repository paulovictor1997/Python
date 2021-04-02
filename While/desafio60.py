n = int(input('Digite um número : para saber o seu fatorial : '))
c = n
f = 1
while c > 0:
    print('{}'.format(c),end='')
    print(' x ' if c > 1 else ' = ',end='') # gambiarra para  se o valor de C, for maior que 1, ele pegao sinal de igual
    f *= c
    c -= 1
print('{}'.format(f),end='')