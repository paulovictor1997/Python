nome = str(input('Qual o seu nome ? '))
if nome == 'Paulo':
    print('Nome bonito do cacete !!!')
elif nome == 'João' or nome == 'Maria':
    print('Esse nome é popular no Brasil !')
else:
    print('Seu nome é bem popular')
print('Tenha um bom dia {}'.format(nome))

