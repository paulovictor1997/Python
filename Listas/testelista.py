#num = [2,5,3,7,9]
#num.insert(2,8)
#num.append(10)
#print(f'Foram listados {num}.Tem {len(num)} elementos nessa lista')

#num = []
#for cont in range(0,4):
     #num.append(int(input('Digite um valor : ')))
#for p,v in enumerate(num):
    #print(f'Na posição {p} encontrei o valor {v} !')
#print('FIM')
#------------------------------------
#a = [2,4,6]
#b = a[:]
#b[2] = 8
#print(f'Lista A : {a}')
#print(f'Lista B : {b}')
#-------------------------------------
#teste = []
#teste.append('Paulo')
#teste.append(23)
#galera = []
#galera.append(teste [:])
#teste [0] = 'Victor'
#teste [1] = 22
#galera.append(teste [:])
#print(galera)

#pessoa = ['Paulo',23] , ['Victor',22] , ['Feitosa',21] , ['Nunes',20]
#for p in pessoa:
#    print(f'{p[0]} tem {p[1]} anos de idade !')
#print('FIM')

galera = []
dado = []
totmaior  = totmenor = 0
for c in range(0,3):
    dado.append(str(input('Nome : ')))
    dado.append(int(input('idade : ')))
    galera.append(dado[:])
    dado.clear()
for p in galera:
    if p[1] > 18:
        print(f'{p[0]} é maior de idade !')
        totmaior += 1
    else:
        print(f'{p[0]} é menor de idade !')
        totmenor += 1
print(f'Temos {totmaior} maiores e {totmenor} menores de idade !')