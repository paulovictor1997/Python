def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except(ValueError,TypeError):
            print('Erro! Digite novamente um número inteiro válido ! ')
            continue
        except(KeyboardInterrupt):
            print('O usuário não Informou esse número !')
            return 0
        else:
            return n


def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
        except(ValueError,TypeError):
            print('Erro, digite novamente um número real válido !')
        except(KeyboardInterrupt):
            print('O usuário não informou esse número !')
            return 0
        else:
            return n


n1 = leiaInt('Informe um número inteiro : ')
n2 = leiaFloat('Informe um número real : ')
print(f'O valor inteiro digitado foi : {n1} . O valor real digitado foi : {n2}')