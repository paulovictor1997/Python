from time import  sleep
print('----------TABUADA----------')
print('PARA SAIR DIGITE UM NÚMERO NEGATIVO !')
print('-' * 27)
while True:
    num = int(input('Qual número você quer saber a tabuada ?! '))
    if num < 0:
        print('TABUADA ENCERRADA')
        break
    sleep(1)
    for cont in range (1,11):
        mult = num * cont
        print(f'{num} X {cont} = {mult}')
