print('VERIFICADOR DE VOGAIS')
print('-='*20)
palavra = ('computador','aprender','programar','linguagem')
for p in palavra:
    print(f'\nNa palavra {p} temos : ',end=' ')
    for letra in p:
        if letra in p:
            if letra.lower() in 'aeiou':
                print(letra,end=' ')
print('\nFIM')