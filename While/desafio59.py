from time import sleep
n = int(input('Digite um valor : '))
n2 = int(input('Informe outro valor :  '))
resultado = 0
while resultado != 5 :
  resultado = int(input('''Informe uma das opções 
  [1] SOMAR
  [2] MULTIPLICAR
  [3] MAIOR  
  [4] NOVOS NÚMEROS
  [5] SAIR DO PROGRAMA \n'''))
  if resultado == 1:
      soma = n + n2
      print('A soma dos valores foi : {}'.format(soma))
      print('-=' * 20)
  elif resultado == 2:
      mult = n * n2
      print('A multiplicação dos números é : {}'.format(mult))
      print('-=' * 20)
  elif resultado == 3:
     if n > n2:
        maior = n
     else: maior = n2
     print('O maior informado foi : {}'.format(maior))
     print('-=' * 20)
  elif resultado == 4:
      n = int(input('Digite um valor : '))
      n2 = int(input('Informe outro valor :  '))
  elif resultado == 5:
      sleep(1)
      print('-='* 20)
      print('FIM')
  else:
   print('Opção ínvalida  ')
