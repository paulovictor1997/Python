def fatorial(n,show = False):
    '''
    -> Calculo de Fatorial
    :param n: Número a ser calculado
    :param show: Comando opcional, ser for alterado para True, ele mostrará o calculo detalhado
    :return: O valor do fatorial de n
    '''
    f = 1
    for c in range(n,0,-1):
        if show:
            print(c, end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        f *= c
    return f


#Programa principal
numero = int(input('Digite o número para saber seu fatorial : '))
print(fatorial(numero,show=True))

