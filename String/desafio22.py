nome = str(input('Seu nome completo : ')).strip()
print('O nome todo maiúsculo : {}' .format(nome.upper()))
print('O nome todo minúsculo : {}' .format(nome.lower()))
print('A quantidade de letras ao todo é : {} letras'.format(len(nome) - nome.count(' ')))
dividir = nome.split()
print('Seu primeiro nome é {} e tem : {} letras'.format(dividir[0], len(dividir[0])))

#print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))


