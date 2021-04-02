maior = 0
menor = 0
for p in range(1,6):
    peso = float(input('Informe o {}º peso : '.format(p)))
    if p == 1:
        maior = peso  #método usado onde ele sempre verá a primeira opção sendo o maior e o menor peso !
        menor = peso
    else:
        if peso > maior: #Já aqui, caso a primeira opção não seja mais o menor peso, ele irá verificar as outras opções
            maior = peso
        if peso < menor:
            menor = peso
print('O maior peso é de : {}kg'.format(maior))
print('O menor peso é de : {}kg'.format(menor))



