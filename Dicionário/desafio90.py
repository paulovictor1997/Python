ficha = {}
ficha['nome'] = str(input('Nome : '))
ficha['média'] = float(input(f'Média do {ficha["nome"]} : '))
print('-='*10)
print(f'O nome do aluno(a) é {ficha["nome"]}. E sua média é : {ficha["média"]}')
if ficha['média'] >=6:
    print('Aluno(a) aprovado(a) !')
else:
    print('Aluno(a) reprovado(a) !')