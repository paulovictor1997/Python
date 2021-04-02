nota1 = float (input('Digite a primeira nota : '))
nota2 = float(input('Digite a segunda nota : '))

média = (nota1 + nota2)/2

if média < 5.0:
    print('O aluno está reprovado !')
elif média > 5.0 and média < 6.9:
    print('O aluno está de recuperação !')
else:
    média >= 7.0
    print('O aluno está aprovado !')