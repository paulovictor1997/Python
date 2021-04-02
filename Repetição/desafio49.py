valor = int(input("Digite o valor para saber a sua tabuada : "))
for n in range(1,11):
    mutl = valor * n
    print('\033[36m{} x {} = \033[31m{}'.format(valor,n,mutl))


