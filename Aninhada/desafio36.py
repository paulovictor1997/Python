print('VERIFICAÇÃO DE EMPRÉSTIMO ')
print('-'*20)
imovel = float(input('Qual o valor da casa ? '))
salario = float(input('Qual o salário do comprador ? '))
ano = int(input('Quantos anos pretende pagar ? '))
valor = imovel / (ano * 12)
mínimo = salario * 30 / 100
print('Para pagar uma casa de {:.2f}$ em {} anos,'.format(imovel,ano), end='')
print('a prestação será de {:.2f}$'.format(valor))
if valor <= mínimo:
    print('O empréstimo pode ser aprovado !!!')
else:
    print('O empréstimo não pode ser aprovado !!!')