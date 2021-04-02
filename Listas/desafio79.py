numero = []
while True:
     num= int(input('Infome o valor : '))
     if num in numero:
         print('Valor já inserido !')
         num = int(input('Infome o valor : '))
     numero.append(num)
     continuar = ' '
     while continuar not in 'SN':
      continuar = str(input('Deseja continuar [S/N] ? ')).strip().upper()
     if continuar == 'N':
         break
numero.sort()
print(f'Foram adicionados na lista : {numero}')


