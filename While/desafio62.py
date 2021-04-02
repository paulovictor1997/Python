print('--------- Progressão Aritimética ---------- ')
print('-='*20)
primeiro = int(input('Informe o primeiro termo : '))
razão = int(input('Informe a razão : '))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total :
        print('{} -'.format(termo),end='')
        termo += razão
        cont += 1
    print('PAUSE')
    mais = int(input('Quantos termos quer mostrar mais ? '))
print('Progressão finalizada, foi mostrado {} termos !'.format(total))
print('FIM')