nome=input('Informe seu nome :')
idade1=input('Informe a idade :')
peso1=input('Informe seu peso :')
print('-------------------------')

nome=input('Informe seu nome :')
idade2=input('Informe sua idade :')
peso2=input('Informe seu peso :')
print('-------------------------')

print('A soma das idades são :',int(idade1)+int(idade2))
print('A soma dos pesos são :',float(peso1)+float(peso2))
print('-------------------------')

print('O tipo primitivo é :',type(nome),type(idade1),peso1)
print('É alfabético :',(nome.isalpha()))
print('É númerico :',(idade1.isnumeric()))
print('É decimal :',(peso1.isdecimal()))

print('------------------------------------')

print('O tipo primitivo é :',type(nome),type(idade2),type(peso2))
print('É alfabético :',(nome.isalpha()))
print('É númerico :',(idade2.isnumeric()))
print('É decimal :',(peso2.isdecimal()))


