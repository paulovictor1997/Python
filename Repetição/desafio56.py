sidade = 0
midade = 0
midadehomen = 0
nomevelho = ''
totalmulher20 = 0
for p in range(1,5):
    print('-----{} PEESOA-----'.format(p))
    nome = str(input('Nome : ')).strip()
    idade = int(input('Idade : '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    sidade += idade
    if p == 1  and  sexo in 'Mm':
       midade = idade
       nomevelho = nome
    if sexo  in 'Mm' and idade > midade:
       midadehomen = idade
       nomevelho = nome
    if sexo in 'Ff' and idade < 20:
       totalmulher20 += 1
print('-=' * 10)
midade = sidade/4
print('A média de idade dos grupos é : {} anos '.format(midade))
print('O homem mais velho se chama {} e tem {} ano(s)'.format(nomevelho,idade))
print('Ao todo são {} mulheres com menos de 20 anos !'.format(totalmulher20))