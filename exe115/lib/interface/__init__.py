def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except(ValueError,TypeError):
            print('Erro ! Digite novamente.')
            continue
        except(KeyboardInterrupt):
            return 0
        else:
            return n


def linha(tam = 40):
    return '-' * tam


def cabeçalho(txt):
    print(linha())
    print(txt.center(40))
    print(linha())


def menu(lista):
   cabeçalho('MENU PRINCIPAL')
   c = 1
   for item in lista:
       print(f'\033[33m{c} - \033[34m{item}')
       c+=1
   print(linha())
   opcao = leiaInt('\033[32mSua opção : \033[m')
   return opcao
