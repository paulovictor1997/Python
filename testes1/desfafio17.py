from math import hypot
coposto = float(input('Informe o cateto oposto :'))
cadjacente = float(input('Informe o cateto adjacente :'))
hipotenusa = hypot(coposto,cadjacente)

print('O valor da hipotenusa é : {:.2f}'.format(hipotenusa))