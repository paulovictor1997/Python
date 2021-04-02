from random import randint
print('---------ADVINHE O NÚMERO QUE EU ESTOU PENSANDO---------')
jogador = int(input('Digite um número ! ' ))
palpites = 0
computador = randint(0,10)
while jogador != computador:
    jogador = int(input('Tente novamente ! '))
    palpites += 1
if jogador == computador:
    print('Parabéns o número foi {},você acertou, foram necessários {} tentativa(s)'.format(jogador,palpites))
print('FIM DE JOGO !')
