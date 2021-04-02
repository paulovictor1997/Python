print('--------- Progressão Aritimética ---------- ')
print('-='*20)
primeiro = int(input('Informe o primeiro termo : '))
razão = int(input('Informe a razão da PA : '))
termo = primeiro  #Aqui ele vai mostrar o termo
cont = 1  #Aqui ele vai contar os termos
while cont <=10:
    print('{} - '.format(termo), end= '')
    termo += razão
    cont += 1
print('FIM')