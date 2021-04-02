numero = int(input('Digite um número : '))
divisao = numero//2
#No "if",se o número dividido por dois, for igual a zero, o número será par, caso contrário,impar.
if (numero % 2) == 0 :
    print('O número {} é par'.format(numero).format(divisao))
else:
    print('O número {} é impar'.format(numero))