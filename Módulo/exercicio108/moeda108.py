def dobro(n=0):
    ret = n * 2
    return ret


def metade(n=0):
    ret = n / 2
    return ret


def aumentar(n=0):
    ret = n + (n * 10/100)
    return ret


def diminuir(n=0):
    ret = n - (n * 13/100)
    return ret


def moeda(preço=0, moeda='R$' ):
    return f'{preço}{moeda:}'.replace('.' , ',')