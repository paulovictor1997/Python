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