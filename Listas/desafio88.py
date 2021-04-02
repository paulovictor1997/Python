from random import randint
from time import sleep
lista = []
jogo = []
print('-='*20)
print('             MEGA SENA           ')
print('-='*20)
quantidade = int(input('Quantos jogos você quer que seja sorteado : '))
tot = 1
while tot <= quantidade:
    cont = 0
    while True:
        num = randint(1,60)
        if num not in lista:
            lista.append(num)
            cont +=1
        if cont >=6:
            break
    lista.sort()
    jogo.append(lista[:])
    lista.clear()
    tot+=1
print(f'Sorteando {quantidade} jogos...')
for i,l in enumerate(jogo):
    print(f'jogo {i+1} : {l}')
    sleep(1)
print('FIM')
