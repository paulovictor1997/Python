def moeda(real):
    while True:
        opcao = int(input('''Digite a opção para a moeda ser convertida : 
          [1] DOLAR
          [2] EURO
          [3] LIBRA
          [4] DIGITAR NOVAMENTE
          [5] SAIR \n'''))
        if opcao == 1:
            dolar = real / 5.13
            print(f'O valor convertido será de : {dolar:.2f} dolares')
        if opcao == 2:
            euro = real / 6.28
            print(f'O valor convertido será de : {euro:.2f} euros ')
        if opcao == 3:
            libra = real / 6.91
            print(f'O valor covnertido será de : {libra:.2f} libras')
        if opcao == 4:
            num = int(input('Digite um novo valor : '))
        if opcao == 5:
            print('VOLTE SEMPRE')
            break




        #continuar = ' '
        #while continuar not in 'SN':
           #continuar = str(input('Deseja continuar ? [S/N] : ')).strip().upper()
        #if continuar == 'N':
            #print('VOLTE SEMPRE')
            #break

