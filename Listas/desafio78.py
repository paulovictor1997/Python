numero = []
maior = []
menor = []
for cont in range(0,5):
    numero.append(int(input(f'Digite um valor na posição {cont} : ')))
print('-='*20)
print(f'Os valores digitados foram : {numero}')
for pos, valor in enumerate(numero):
    if valor == max(numero):
       maior.append(pos)
    if valor == min(numero):
        menor.append(pos)
print(f'O maior valor foi {max(numero)}, nas posições {maior}',end='...\n')
print(f'O menor valor foi {min(numero)},nas posições {menor}',end='...')







