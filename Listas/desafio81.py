lista =[]
while True:
    lista.append( int(input('Digite um valor : ')))
    continuar = ' '
    while continuar not in 'SN':
     continuar = str(input('Dseja continuar [S/N] ?! ')).strip().upper()
    if continuar == 'N':
        break
if 5 in lista:
     print('O número 5 está na lista')
print(f'Na lista tem {len(lista)} elemetos')
lista.sort(reverse = True)
print(f'A lista em ordem decresente {lista}')





