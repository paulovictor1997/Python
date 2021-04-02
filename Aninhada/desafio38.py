numero1 = int(input('Digite o primeiro valor : '))
numero2 = int(input('Digite o segundo valor : '))

maior = numero1
if numero1 > numero2:
    print('O primeiro valor é maior'.format(maior))
elif numero1 == numero2:
    print('Não existe um valor maior, os dois são iguais !')
else:
    numero2 > numero1
    print('O segundo valor é maior !'.format(maior))