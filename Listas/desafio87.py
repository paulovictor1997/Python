matriz = [[0],[0],[0]],[[0],[0],[0]],[[0],[0],[0]]
par = tercol = 0
for l in range (0,3):
  for c in range (0,3):
      matriz[l][c] = int(input(f'Diite os valores na matriz, na posição {l},{c} : '))
print('-='*30)
for l in range (0,3):
    for c in range (0,3):
        print(f'[{matriz[l][c] :^5}]',end='')
        if matriz[l][c] %2 == 0:
            par += matriz[l][c]
    print()
for l in range (0,3):
    tercol+=matriz[l][2]

print('-='*30)
print(f'A soma dos valores pares são : {par}')
print(f'A soma dos valores  para a terceira coluna é : {tercol}')
print(f'O maior valor da segunda linha é : {max(matriz[1])}')