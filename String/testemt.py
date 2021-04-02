frase = str(input('Digite uma frase : ')).strip()
print('Sua frase teme o total de {} caracteres !'.format(len(frase)))
dividir = frase.split()
print('A primeira palavra da frase digitada foi : {}'.format(dividir[0]).format(frase))
print('A última palavra da frase digitada foi : {}'.format(dividir[-1]).format(frase))

print('---------------------------------------------')

fraseb = str(input('Digite qualquer frase : '))
print('Na frase tem Maceió : {} '.format('Maceió'in fraseb))
