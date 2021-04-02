from datetime import date
ano = int(input('Digite o ano para saber se é bissexto, digite 0, para saber o ano atual : '))
dividir = ano//4
if ano == 0:
    ano = date.today().year
if (ano % 4 == 0) and (ano % 100 != 0) or ano % 400 == 0:
    print('O ano de {} é bissexto'.format(ano))
else:
    print('O ano {} não é bissexto'.format(ano))

#Assim como o exercicío do par ou impar,
#nesse cdalculo o programa irá pegar verificar
#se o resto da divisão por 4 seja zero, para
#identificar se o ano é bissexto,porém, o ano
#não pode ser divisivél por 100, com isso a
#divisão fica exata,ou seja, deixa o resto
#diferente de zero.
