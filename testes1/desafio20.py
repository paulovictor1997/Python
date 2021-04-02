from random import shuffle
print('Sorteio para apresentação !!!')

grupo1 = input('Primero grupo : ')
grupo2 = input('Segundo grupo : ')
grupo3 = input('Terceiro grupo : ')
grupo4 = input('Quarto grupo : ')

sorteio = [grupo1,grupo2,grupo3,grupo4]
shuffle(sorteio)
print(f'A ordem de apresentação é : {sorteio}')
#print(sorteio)