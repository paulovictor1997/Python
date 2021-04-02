from time import sleep
ficha = []
while True:
    nome = str(input('Nome : '))
    nota1 = float(input('Primeira nota : '))
    nota2 = float(input('Segunda nota : '))
    media = (nota1 + nota2 )/2
    ficha.append([nome,[nota1, nota2], media])
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar [S/N] : ')).strip().upper()
    if continuar == 'N':
         break
print('-='*20)
print(f'{"Nº":<4}{"NOME ":<10}{"MÉDIA":>8}')
print('-='*20)
for i, a, in enumerate(ficha):
    print(f'{i : <4}{a[0]:<10}{a[2] : >8}')
while True:
    print('-='*20)
    opção = int(input('Mostrar nota de qual aluno (Digite 999 para sair)? '))
    if opção ==  999:
        break
    if opção <=len(ficha)-1:
        print(f'Notas de {ficha[opção][0]} são {ficha[opção][1]}')
sleep(1)
print('VOLTE QUANDO QUISER')