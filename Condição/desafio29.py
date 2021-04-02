km = float(input('Informe quantos km foram rodados : '))
pago = ( km - 80 ) * 7
if km > 80:
    print('Você ultrapassou o limite, você vai pagar {} reais !'.format(pago))
else:
    print('Você não ultrapassou o limite, pode seguir !')
#o valor da multa será a subtração entre a quilometragem e o limite da velocidade, multiplicado por 7