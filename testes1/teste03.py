n=input('Digite algo :')

print('O tipo primitivo é :',(type(n)))
print('Esse é númerico :',(n.isnumeric()))
print('É alfabético :',(n.isalpha()))
print('É decimal :',(n.isdecimal()))
print('É maiúsculo :',(n.isupper()))
print('É minúsculo :',(n.islower()))
print('É alphanum :',(n.isalnum()))
print('Está capitalizada :',(n.istitle()))

print('Fim da verificação !!!')
