km=float(input('Informe por quantos km você irá viajar : '))
passagem = km * 0.50
if km <= 200:
    print('O valor da sua passagem será de \033[0;33:m {} \033[m reais'.format(passagem))
else:
    passagem = km * 0.45
    print('Se a viagem passar de 200 km, o valor da passagem será {} reais'.format(passagem))