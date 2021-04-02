numero = [[],[]]
for cont in range(1,8):
    num = int(input(f'Digite o {cont}º valor : '))
    if num % 2 == 0:
     numero[0].append(num)
    else:
      numero[1].append(num)
numero[0].sort()
print(f'Os números pares citados : {numero[0]}')
numero[1].sort()
print(f'Os números ímpares citados : {numero[1]}')
