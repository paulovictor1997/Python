time = []
jogador = {}
partidas = []
while True:
    jogador.clear()
    jogador['nome']= (str(input('Nome do jogador : ')))
    total = int(input(f'Quantas partidas {jogador["nome"]} jogou ?! '))
    partidas.clear()
    for c in range(0, total):
        partidas.append(int(input(f'Gols marcados na partida {c+1} : ')))
    jogador['gol'] = partidas[:]
    jogador['total'] = sum(partidas)
    time.append(jogador.copy())
    while True:
        continuar =  str(input('Deseja continuar [S/N] ? ')).strip().upper()
        if continuar in 'SN':
            break
        print('Digite apenas S ou N !')
    if continuar == 'N':
        break
print('-='*30)
print('Cod',end='')
for i in jogador.keys():
    print(f'{i:<15}',end='')
print()
print('-='*40)
for k,v in enumerate(time):
    print(f'{k:>3} ',end='')
    for d in v.values():
        print(f'{str(d):<15}',end='')
    print()
print('-='*40)
while True:
    busca = int(input('Mostrar dados de qual jogador (Digite 999 para sair )?! '))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'Erro !!! Não existe jogador com o código {busca} !')
    else:
        print(f'LEVANTAMENTO DO JOGADOR {time[busca]["nome"]}')
        for i,g in enumerate(time[busca]["gol"]):
            print(f'No jogo {i+1} fez {g} gols.')
    print('-'*40)
print('FIM')