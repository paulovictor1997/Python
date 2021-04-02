numero = quant = soma = 0
while True:
    numero = int(input("Digite um valor (Pressione 999 para parar ) : "))
    if numero == 999:
        break
    soma += numero
    quant += 1
print('-='*20)
print(f'Foram digitados {quant} número(s) e a soma é : {soma}')
print('FIM')