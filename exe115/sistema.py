from exe115.lib.interface import *
from exe115.lib.arquivo import *
from time import sleep
arq = 'doc.txt'
if not arquivoExiste(arq):
        criarArquivo(arq)

while True:
    resposta = menu(['Ver pessoas cadastradas','Cadastrar','SAIR'])
    if resposta == 1:
        #Aqui vai listar o conteúdo do arquivo
        lerArquivo(arq)
    elif resposta == 2:
        #Cadastrar uma nova pessoa
        cabeçalho('Novo Cadastro')
        nome = str(input('Nome : '))
        idade = leiaInt('Idade : ')
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        cabeçalho('\033[34mSaindo...Volte sempre !\033[m')
        break
    else:
        print('\033[31mErro... Digite novamente !\033[m')
    sleep(1)