temp = []
lista = []
maior = menor = 0
while True:
    temp.append(str(input('Nome : ')).strip())
    temp.append( float(input('Peso : ')))
    if len(lista) == 0:
        maior = menor = temp[1]
    else:
        if temp[1] > maior:
            maior = temp[1]
        if temp[1] < menor:
            menor = temp[1]
    lista.append(temp[:])
    temp.clear()
    continuar = ' '
    while continuar not in 'SN':
        continuar  = str(input('Deseja continuar [S/N] ? ')).strip().upper()
    if continuar == 'N':
        break
print(f'-='*20)
print(f'Foram cadastradas {len(lista)} pesssoas')
print(f'Os maiores peso foi de {maior}KG.Peso de :',end=' ')
for p in lista:
    if p[1] == maior:
     print(f'[{p[0]}]',end=',')
print()
print(f'Os menores peso foi de {menor}KG.Peso de :',end=' ')
for p in lista:
    if p[1] == menor:
        print(f'[{p[0]}]',end=',')