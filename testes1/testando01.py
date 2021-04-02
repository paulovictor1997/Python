from math import pow,sqrt,factorial
num = int(input("Digite o número : "))
num1 = int(input('Iforme a potência que deseja ser calculada : '))
expoente = pow(num,num1)
print('O número {}, elevado a potência informada é : {} '.format(num,expoente))

print('----------------------------------------------------------------------')

numero = int(input('Informe o número para descobrir sua raiz quadrada : '))
raiz = sqrt(numero)
print('A raiz quadrada é : {:.2f}'.format(raiz))

print('--------------------------------------------------------------------')

número = int(input('Digite o número para saber seu valor fatorial :'))
fatorial = factorial(número)
print('O resultado da fatorial é : {}'.format(fatorial))

