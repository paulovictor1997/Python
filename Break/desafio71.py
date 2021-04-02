print('CAIXA ELETRÔNICO') #Considerar notas de 1,10,20,50
print('-'*16)
valor = int(input('Digite o valor que quer sacar R$ : '))
total = valor
cedula = 50 #Começo declarando com a maior cédula
totcedula = 0
while True:
    if total >= cedula:
        total -=cedula #Nessa função a cada vez que o valor do saque for maior que 50
        totcedula +=1 # ele irá tirando o valor quantas vezes for necessário
    else:
        if totcedula > 0:
            print(f'Foram tiradas o total de {totcedula} cédula(s) de {cedula}')
        if cedula == 50:    #A partir daqui com isso,
           cedula = 20      #se a cédula atual não for 50, ele vai tirando 50 do valor e assim por diante
        elif cedula == 20:
             cedula = 10
        elif cedula == 10:
            cedula = 1
        totcedula = 0
        if total == 0:
            break
print('-'*20)
print('Operação Encerrada !')


