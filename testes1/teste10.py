real=float(input('Digite seu valor em real :\n'))

dolar = real/5.33
euro = real/5.82
libra = real/6.55

print('Com o valor de {} reais, você pode comprar {:.2f} dolares'.format(real,dolar))
print('Com o valor de {} reais, você pode comprar {:.2f} euros'.format(real,euro))
print('Com o valor de {} reais, você pode comprar {:.2f} libras'.format(real,libra))