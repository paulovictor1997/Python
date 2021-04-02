def dobro(n=0,formatado = False):
    ret = n * 2
    return ret if formatado is False else moeda(ret)


def metade(n=0,formatado = False):
    ret = n / 2
    return ret if formatado is False else moeda(ret)


def aumentar(n=0,formatado = False):
    ret = n + (n * 10/100)
    return ret if formatado is False else moeda(ret)


def diminuir(n=0,formatado = False):
    ret = n - (n * 13/100)
    return ret if not formatado else moeda(ret)


def moeda(preço=0, moeda='R$' ):
    return f'{preço}{moeda:}'.replace('.' , ',')


def resumo(preço = 0):
    print('-'*30)
    print(f'RESUMO DAS TAXAS '.center(30))
    print('-'*30)
    print(f'O preço informado foi : \t{moeda(preço)}')
    print(f'A metade do preço : \t\t{metade(preço,True)} ')
    print(f'O dobro do preço : \t\t\t{dobro(preço,True)}')
    print(f'Com aumento 10% : \t\t\t{aumentar(preço,True)}')
    print(f'Com desconto de 13% : \t\t{diminuir(preço,True)} ')
    print('-'*30)
    print('-'*30)