print('Formador de triângulos ')
print('-='*20)
reta1 = float(input('Primeira reta : '))
reta2 = float(input('Segunda reta : '))
reta3 = float(input('Terceira reta : '))
if reta1 < reta2 + reta3 and reta2 < reta1 + reta3  and reta3 < reta1 + reta2:
    print('As retas podem formar um triangulo !')
else:
    print('As retas não podem formar um triângulo !')