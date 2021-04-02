from exercicio108 import moeda108
preço = float(input('Digite o preço : '))
print(f'A metdade de {moeda108.moeda(preço)} é : {moeda108.moeda(moeda108.metade(preço))}')
print(f'O dorbro de {moeda108.moeda(preço)} é : {moeda108.moeda(moeda108.dobro(preço))}')
print(f'O preço de {moeda108.moeda(preço)} aumentado em 10% é : {moeda108.moeda(moeda108.aumentar(preço))} ')
print(f'O preço de {moeda108.moeda(preço)} com 13% de desconto é {moeda108.moeda(moeda108.diminuir(preço))}')