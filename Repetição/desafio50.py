par = 0
soma = 0
for s in range(6):
     numero = int(input('Informe um número : '))
     if numero % 2 == 0:
      soma = soma + numero
      par = par + 1
print('-'*20)
print('Existem {} número(s) pares e a soma deles é : \033[0;31m{} '.format(par,soma))







