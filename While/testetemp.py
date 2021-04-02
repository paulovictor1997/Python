from time import sleep
print('----------CONVERSÃO DE TEMPERATURAS----------')
temp=float(input('Informe a temperatura para ser convertida : '))
opcao = 0
while opcao !=8:
    opcao = int(input('''Informe a oção que queira ser convertida :
    [1] CELSIUS para KELVIN
    [2] CELSIUS para FAHRENHEINT
    [3] FAHRENHEINT para CELSIUS 
    [4] KELVIN para CELSIUS 
    [5] KELVIN para FAHRENHEINT
    [6] FAHRENHEINT para KELVIN
    [7] Digitar novamente  
    [8] SAIR \n'''))
    if opcao == 1:
        kelvin = temp + 273
        print('A conversão de {}C°, para KELVIN é : {:.2f}K'.format(temp,kelvin))
        print('-='*20)
    if opcao == 2:
        fah = (temp * 9/5) + 32
        print('A conversão de {}C°, para FAHRENHEINT é : {:.2f}F'.format(temp,fah))
        print('-=' * 20)
    if opcao == 3:
        f = (temp - 32) * 5/9
        print('A conversã de {}F°, para CELSIUS é : {:.2f}°C'.format(temp,f))
        print('-=' * 20)
    if opcao == 4:
       celsius = temp - 273
       print('A conversão de {}°K, para CELSIUS é : {:.2f}°K'.format(temp,celsius))
       print('-=' * 20)
    if opcao == 5:
        k = (temp - 273) * 9 / 5 + 32
        print('A conversão de {}°K, para FAHRENHEINT é : {:.2f}°K'.format(temp, k))
        print('-=' * 20)
    if opcao == 6:
      fa = (temp - 273) * 9 / 5 + 273
      print('A conversão de {}°F, para KELVIN é : {:.2f}°K'.format(temp, fa))
      print('-=' * 20)
    if opcao == 7:
        temp = float(input('Informe a temperatura para ser convertida : '))
        print('-=' * 20)
    if opcao == 8:
       sleep(1)
       print('VOLTE SEMPRE')
    else:
        print('OPÇÃO ÍNVALIDA')