from random import choice
from time import sleep
print('''VAMOS JOGAR PEDRA,PAPEL E TESOURA,ESCOLHA UMA DAS OPÇÕES :
[1] PEDRA
[2] PAPEL
[3] TESOURA ''')
print('-'*20)
jogador = str(input('DIGITE A SUA OPÇÃO : ')).strip()
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO')
lista = ['pedra','papel','tesoura']
jogo = choice(lista)
print('O computador escolheu {}'.format(jogo))

if jogador == jogo:
    print('Empate,jogue novamente !!!')
elif jogador == 'papel' and jogo == 'pedra' or jogador == 'tesoura' and jogo == 'papel' or jogador == 'pedra' and jogo== 'tesoura':
    print('VOCÊ GANHOU !!!')
elif jogo == 'papel' and jogador == 'pedra' or jogo == 'tesoura' and jogador == 'papel' or jogo == 'pedra' and jogador == 'tesoura':
    print('O COMPUTADOR VENCEU !!!')

#Usando randint : coloco o lista no format entre os colchetes