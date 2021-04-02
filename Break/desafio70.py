print('VERIFICAÇÂO DE PREÇOS')
print('-'*20)
total = mil = menor = cont = 0
barato = ' '
while True :
    produto = str(input('Digite o nome do produto : '))
    preço = float(input('Preço  R$ : '))
    total +=preço
    cont += 1 #vai contar quantos preços eu tenho
    if preço > 1000:
        mil +=1
    if cont == 1 or preço < menor: #Se o preço for igual ao 1ºno contadpr , ele passa a ser o menor preço,
        menor = preço #mas se o preço for menor que o preço, o "menor", passa a ser o menor digitado.
        barato = produto
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Deseja Continuar [S/N] : ')).strip().upper()[0]
    if continuar == 'N':
        break
print('FIM')
print(f'O valor total da compra é : {total} ')
print(f'{mil} produto(s) passaram dos R$1000.00 reais .')
print(f'O produto mais barato foi {barato} e custa : {menor}')