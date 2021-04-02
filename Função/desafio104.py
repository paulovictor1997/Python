def leiaInt(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print(f'\033[0;31mErro !!! Digite novamente. \033[m')
        if ok:
            break
    return valor


n = leiaInt('Digite um número : ')
print(f'O número digitado foi : {n}')