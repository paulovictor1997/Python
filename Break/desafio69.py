print('CADASTRO')
quant = quanthomen = mulher20 = 0
while True:
    idade = int(input('IDADE : '))
    if idade > 18:
        quant +=1
    sexo = ' '
    while sexo not in 'MF': #CASO O USUÁRIO ERRE NA HORA DE DIGITAR ELE IRÁ REPETIR
     sexo = str(input('[M/F] : ')).strip().upper()[0]
    if sexo in 'Mm':
        quanthomen+=1
    if sexo in 'Ff' and idade < 20:
     mulher20+=1
     print('='*20)
    continuar = str(input('DEJESA CONTINUAR [S/N] : ')).strip().upper()[0]
    print('='*20)
    if continuar in 'Nn':
        print('FIM')
        break
print(f'Pessoas com mais de 18 anos : {quant}')
print(f'Foram cadastrados {quanthomen} homens !')
print(f'Existem {mulher20} mulher(s) com menos de 20 anos')