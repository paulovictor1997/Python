dados = {}
partida = []
dados['nome'] = str(input('Nome do jogador : '))
total = int(input(f'Quantas partidas {dados["nome"]} jogou ?! '))
for q in range(total):
    partida.append(int(input(f'Quantos gols na partida {q} : ')))
dados['gols'] = partida[:]
dados['total'] = sum(partida)
print('-='*30)
print(dados)
print('-='*30)
for k, v in dados.items():
    print(f'O campo {k} tem o valor {v}')
print('-='*30)
print(f'O jogador {dados["nome"]}, jogou {len(dados["gols"])} partidas')
for i,v in enumerate(dados['gols']):
    print(f' => Na partida {i}, fez {v} gols ')
print(f'Total de gols feitos : {dados["total"]} gols')