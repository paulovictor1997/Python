n = int(input('Digite um valor, para saber o seu fatorial : '))
fator = n
for c in range(n-1,0,-1):
    n = n * c
print('O fatorial é : {}'.format(n))