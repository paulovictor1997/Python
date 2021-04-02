numero = ('zero','um','dois','três','quatro','cinco','seis','sete','oito','nove','dez'
          'onze','doze','treze','quatorze','quinze','dezesseis','dezessete','dezoito'
          'dezenove','vinte')
while True:
    num = int(input('Digite um número de 0 à 20 : '))
    if num < 0 or num > 20:
        print('Tente novamente.',end='')
    else:
         print(f'Você digitou o número : {numero[num]}')
    cont = ' '
    while cont not in 'SN':
     cont  = str(input('Deseja continuar [S/N] : ')).strip().upper()[0]
    if cont == 'N':
        break
print('FIM DO PROGRAMA')

#if 0 <= num <=20:
    #    break
     #   print('Tente novamente.', end='')
#print(f'Você digitou o número : {numero[num]}')
#(Solução do exercício)







