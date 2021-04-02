ano = int(input('Digtite o ano do seu nascimento : '))
idade = 2020 - ano
prazo = 18 - idade
if idade < 18:
    print('Você tem {} anos, faltam {} ano(s) para você se alistar'.format(idade,prazo))
elif idade == 18:
    print('Já está na hora de se apresentar ao serviço militar !')
else:
    idade > 18
    print('Você tem {} anos, você passou {} ano(s) do prazo !'.format(idade,prazo * -1))
    # para converter a o número para positivo, multiplico por -1

    ##OUTRA MANEIRA DE FAZER ###
#from datetime import date
#atual = date.today().year
#ano = int(input('Digtite o ano do seu nascimento : '))
#idade = atual - ano
#print('Quem nasceu em {},tem {} ano(s)_em {}.format(ano,idade,atual)')
#if idade == 18:
#print('Tem que se alistar')
#elif idade < 18:
#saldo = 18 - idade
#print('Ainda falta {} ano(s) para se alistar'.format(saldo))
#ano = atual + saldo
#print('Seu ano de alistametto será {}'.format(ano))
#elif > 18:
#saldo = idade - 18
#print('Você já deveria ter se alistado há {} ano(s).'.format(saldo))
#ano = atual - saldo
#print('Seu alistamento foi em {}.format(ano) ')