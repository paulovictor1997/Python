salario = float(input('Informe seu salário : '))
if salario <= 1250:
    novo = salario + (salario * 15 / 100)
    print('Seu salário atual com aumento de 15%, ele fica {} reais'.format(novo))
else:
    novo = salario + (salario * 10 / 100)
    print('Seu salário atual com aumento de 10%, ele fica {} reais'.format(novo))
 # O calculo será feito como : o salário atual receberá o calculo com a porcentagem
