n1=int(input('Digite a primeira nota :'))
n2=int(input('Digite a segunda nota :'))

soma = n1+n2
media = soma/2

print('A soma é {}, portanto a média é {}'.format(soma,media))

if media >=6:
    print('Aluno aprovado')
if media <6:
    print('Aluno reprovado !')