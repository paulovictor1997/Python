sexo = str(input('Digite à sua opção sexual (M,F): ')).strip().upper()[0]
while sexo not in 'MF':
    sexo = str(input('Deu erro, digite novavente ! ')).strip().upper()[0]
print('O sexo {}, está registrado !'.format(sexo))
