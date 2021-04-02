print('MÚLTIPLOS DE 3 ENTRE 1 E 500  !')
soma = 0 #soma será o acumulador, pois não recebeu nenhum valor !
cont = 0 #será o contador
for n in range(1,501,2):
    if (n % 3 )== 0:
     soma = soma + n
     cont = cont + 1 #a cada vez que ele achar um número divisor de três com o resto de 0, ele somará com +1
print('Os múltiplos de 3 ímpares são {},e somados dá : {} '.format(cont,soma))