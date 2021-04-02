from random import randint
from time import sleep


def sorteio(lista):
   print('Sorteando 5 valores : ', end=' ')
   for n in range(0,5):
       n = randint(1,10)
       lista.append(n)
       print(f'{n}', end=' ', flush=True)
       sleep(1)
   print('FIM')


def somapar(lista):
    soma = 0
    for v in lista:
        if v % 2 == 0:
            soma+= v
    print(f'Somando os valores pares da {lista}, temos : {soma}')


numero = []
sorteio(numero)
somapar(numero)
