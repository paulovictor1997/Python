from exercicio109 import moeda109
preço = float(input('Digite o preço : '))
print(f'A metdade de {moeda109.moeda(preço)} é : {moeda109.metade(preço, True)}')
print(f'O dorbro de {moeda109.moeda(preço)} é : {moeda109.dobro(preço,True)}')
print(f'O preço de {moeda109.moeda(preço)} aumentado em 10% é : {moeda109.aumentar(preço,True)} ')
print(f'O preço de {moeda109.moeda(preço)} com 13% de desconto é {moeda109.diminuir(preço,True)}')