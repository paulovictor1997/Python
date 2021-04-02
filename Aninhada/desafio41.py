ano = int(input('Digite o ano de nascimeto : '))
idade = 2020 - ano
print('Você têm {} anos !'.format(idade))
print('-' *20)

if idade <= 9:
    print('Inscrição na categoria MIRIM ! ')
elif idade > 9 and idade <=14:
    print('Inscrição na categoria INFANTIL !')
elif idade >= 14 and idade <=19:
    print('Inscrição na categoria JÚNIOR !')
elif idade >=19 and idade <=20:
    print('Inscrição na categoria SÊNIOR !')
elif idade > 20:
    print('Inscrição na categoria MASTER !')
