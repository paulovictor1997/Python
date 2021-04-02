numero = (int(input('Digite um número : ')),
          int(input('Digite um número : ')),
          int(input('Digite um número : ')),
          int(input('Digite um número : ')),)
print(f'O número 9 aparece  {numero.count(9)} vezes !')
if 3 in numero:
     print(f'O número 3 aparece na posição : {numero.index(3) + 1}')
else: print('O valor 3 não aparece em nehuma posição ! ')
print('Os valores pares digitados foram :',end=' ' )
for n in numero:
    if n % 2 == 0:
        print(n,end=',')
