from exe115.lib.interface import *
def arquivoExiste(nome):
    try:
        a  = open(nome,'rt') #Read Text, vai ver se o arquivi existe.
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criarArquivo(nome):
    try:
        a = open(nome, 'wt+') #WT Writen Text, vai criar o arquivo.
        a.close()
    except:
        print('\033[31mErro na criação do arquivo \033[m')
    else:
        print(f'Arquivo {nome} criado com sucesso')


def lerArquivo(nome):
    try:
        a = open(nome,'rt')
    except:
        print('Erro ao ler p arquivo !')
    else:
        cabeçalho('PESSSOAS CADASTRADAS ')
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0] : <30}{dado[1]:>3} anos ')
    finally:
        a.close()


def cadastrar(arq,nome = 'desconhecido',idade = 0):
    try:
        a = open(arq,'at')
    except:
        print('Houve um erro na abertura do arquivo !')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('Houve um erro na escritura dos dados !')
        else:
            print(f'Novo registro de {nome} adcionado')
            a.close()