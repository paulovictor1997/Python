numero = []
par = []
impar = []
while True:
    numero.append(int(input('Informe um número : ')))
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar [S/N] : ')).strip().upper()
    if continuar == 'N':
        break
for cont in numero:
    if cont % 2 == 0:
        par.append(cont)
    else:
        impar.append(cont)
print(f'Foram adicionados : {numero}')
print(f'Os números pares são : {par}')
print(f'Os números ímpares são : {impar}')