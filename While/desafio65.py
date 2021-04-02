opção = 'S'
soma = cont = média = maior = menor = 0
while opção in 'Ss':
    n = int(input('Digite um valor : '))
    soma += n
    cont += 1
    if cont == 1:
       maior = menor = n
    else:
     if n > maior :
       maior = n
     if n < menor:
         menor = n
    opção = str(input('Dejesa continuar ? [S/N] ')).strip().upper()[0]
média = soma/cont
print('Foram digitados {} número(s), a média é : {:.2f}'.format(cont,média))
print('O maior número digitado é {} e o menor é {}'.format(maior,menor))
print('FIM')