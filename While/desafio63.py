print('---------SEQUÊNCIA DE FIBONACCI---------')
print('='*40)
numero = int(input('Informe quantos termos queira ver : '))
n1 = 0
n2= 1
print('{} - {}'.format(n1,n2),end= '')
cont = 3
while cont <= numero:
    n3 = n1 + n2
    print(' - {} - '.format(n3),end= '') #Uma vez que o N3 esteja somado,
    n1 = n2  #aqui eu já passo o n1 ser o n2
    n2 = n3  # e o n2 ser o n3
    cont += 1
print('FIM')