from random import randint
print('----------JOGO DO PAR OU ÍMPAR----------')
tentativas = 0
while True:
    jogador = int(input('DIGITE UM VALOR : '))
    computador = randint(0,10)
    total = jogador + computador
    opcao = ' '
    while opcao not in 'PI':
      opcao = str(input('ESCOLHA [PAR/ÍMPAR] : ')).strip().upper()[0]
    print(f'Você jogou {jogador} o comutador jogou {computador}, total : {total}')
    print('DEU PAR' if total %2 == 0  else 'DEU ÍMPAR ')
    if opcao == 'P':
        if total %2 == 0:
            print('VOCÊ VENCEU !')
            tentativas +=1
        else:
            print('VOCÊ PERDEU !')
            break
    elif opcao == 'I':
        if total %2 == 1:
            print('VOCÊ VENCEU ! ')
            tentativas += 1
        else:
            print('VOCÊ PERDEU !')
    print('JOGUE NOVAMENTE ! ')
print(f'FIM DE JOGO , FORAM NECESSÁRIAS : {tentativas} tentativa(s)')