print('Calculo de IMC')
print('-'*20)
peso = float(input("Iforme seu peso : "))
altura = float(input("Iforme sua altura : "))
imc = peso/altura**2
print('Seu IMC é de {:.2f}'.format(imc))

if imc < 18.5:
    print('Você está abaixo do peso !')
elif imc > 18.5 and imc <= 24.9:
    print('Seu peso está ideal !')
elif imc > 25 and imc <= 29.9:
    print('Você está com sobrepeso !')
elif imc > 30 and imc <=39.9:
    print('Você está obeso, precisa emagrecer')
elif imc > 40:
    print('Obesidade mórbida, você precisa urgente emagrecer')