preço = float(input('Informe o preço do produto : '))
print('''ESCOLHA A OPÇÃO DE PAGAMENTO :
[1] pagamento avista dinheiro/cheque, tem 10% de desconto.
[2] avista no cartão, tem 5% de desconto.
[3] duas vezes no cartão, preço normal sem juros
[4] três vezes ou mais no cartão, juros de 20% ''')
pagamento = int(input('A opção foi : '))

if pagamento == 1:
    pagamento = preço - (preço * 10/100)
    print('Você tem 10% de desconto, você vai pagar \033[32m{:.2f} reais'.format(pagamento))
elif pagamento == 2:
    pagamento = preço - (preço * 5/100)
    print('Você tem 10% de desconto, você vai pagar \033[32m{:.2f} reais'.format(pagamento))
elif pagamento == 3:
     pagamento = preço/2
     print('Dividindo em duas vezes no cartão, você irá pagar : \033[32m{} reais '.format(pagamento))
elif pagamento == 4:
    pagamento = preço + (preço * 20/100)
    total = int(input('Quantas parcelas ? '))
    parcela = pagamento/total
    print('Com essa opção pagará 20% de juros, parcelando em {}x, o valor será \033[32m{:.2f} reais'.format(total,parcela))
else:
    print('Escolha somente as opções acima !')
