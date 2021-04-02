#AUMENTAR,DIMINUIR,DOBRO,METADE = PRIMEIRA PARTE DO EXERCÍCIO
from exercicio107 import moeda107
preço = float(input('Digite o preço R$ : '))
print(f'O  preço informado é {preço} e seu dobro é : {moeda107.dobro(preço)} reais')
print(f'A metade do preço informado é : {moeda107.metade(preço)} reais ')
print(f'O preço informado com aumento em 10% é : {moeda107.aumentar(preço)} reais')
print(f'O preço informado com desconto de 13% é : {moeda107.diminuir(preço)} reais ')
