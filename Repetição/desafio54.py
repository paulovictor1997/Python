print('VERFICAÇÃO DE IDADES')
print('-=' * 20)
for d in range(1,8):
    ano = int(input('Digite o ano do seu nascimento : '))
    idade = 2020 - ano
    if idade >= 21:
        print('Você tem {} ano(s), portanto é maior de idade !'.format(idade,ano))
        print('-=' * 20)
    if idade < 21:
        print('Você têm {} ano(s), portanto você é menor de idade'.format(idade,ano))
        print('-=' * 20)

print('FIM DA VERIFICAÇÂO')