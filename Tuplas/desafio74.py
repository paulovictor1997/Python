from random import randint
from time import sleep
numero = (randint(1,10),randint(1,10),randint(1,10),randint(1,10),randint(1,10))
sleep(1)
print(f'Os números sorteados foram : {numero}')
print(f'O maior sorteado foi : {max(numero)}')
print(f'O menor sorteado foi : {min(numero)}')