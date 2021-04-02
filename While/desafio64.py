cont = 0
num = 0
soma = 0
num = int(input('Digite os valores PARA PARAR DIGITE 999 : '))
while num != 999:
     soma += num
     cont += 1
     num = int(input('Digite os valores PARA PARAR DIGITE 999 : ')) #Repetindo esse comando nessa parte de baixo, ele desconsidera o flag !(999)
print('Você digitou {} número(s),A soma é : {}'.format(cont,soma))