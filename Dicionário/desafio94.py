pessoa = []
soma = média = 0
while True:
    dados = {
        'nome': str(input('nome : ')),
        'idade': int(input('idade : ')),
        'sexo' : str(input('sexo [M/F] : ')).strip().upper()
    }
    pessoa.append(dados.copy())
    soma += dados['idade']
    while dados['sexo'] not in 'MF':
       dados['sexo'] = str(input('Digite apenas M/F : ')).strip().upper()
    continuar = ' '
    while continuar not in 'S/N':
        continuar = str(input('Deseja continuar [S/N] ? : ')).strip().upper()
    if continuar == 'N':
        break
print('-='*20)
print(f' - O grupo tem {len(pessoa)} pessoas')
média = soma/len(pessoa)
print(f'A média de idades é : {média:5.2f} anos')
print('As mulheres cadastradas foram : ', end='')
for p in pessoa:
    if p['sexo'] in 'F':
        print(f'{p["nome"]}', end=' - ')
print()
print('-='*20)
print('As pessoas que ficaram acima da média : ')
for p in pessoa:
    if p['idade'] >= média:
        print(' ', end='')
        for k, v in p.items():
            print(f'{k} = {v};', end='')
        print()
print('-='*20)
print('FIM DE PROGRAMA')