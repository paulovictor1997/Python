frase = str(input('Digite uma frase : ')).upper().strip()
print('Quantas vezes aparece a letra "a" ? Aparece {} vezes'.format(frase.count('A')))
print('A letra "a", apareceu pela primeira vez na posição {}'.format(frase.find('A')+1))
print('A última vez que a letra "A" apareceu foi na posição {}'.format(frase.rfind('A')+1))
