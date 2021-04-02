lista = []
for cont in range(0,5):
    numero = int(input('Digite um número : '))
    if cont == 0 or numero > lista[-1]:
        lista.append(numero)
        print('Adicionado no fim da lista.')
    else:
        pos = 0
        while pos <= len(lista):
            if numero<= lista[pos]:
                print(f'Adicionado na posição {pos}')
                lista.insert(pos,numero)
                break
            pos+=1
print('-='*20)
print(f'Os valores adicionados foram : {lista}')