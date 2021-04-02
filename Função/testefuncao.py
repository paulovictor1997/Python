#def soma(a =0,b =0,c = 0):
    #s = a + b + c
    #return s
#s1 = soma(1,2,1)
#s2 = soma(3,1,1)
#print(f'A soma vale : {s1} e {s2}')



#def contador(*num):
    #tam = len(num)
    #print(f'Valores : {num}. E tem {tam} número(s) em cada')


#contador(1 , 3, 5, 7)
#contador(1 , 5 , 7)
#def dobra(lista):
    #pos = 0
    #while pos < len(lista):
        #lista[pos] *= 2
        #pos += 1

#valores = [2,5,4,3]
#dobra(valores)
#print(valores)

#from random import shuffle
#def sorteio(lista):
   # lista = [grupo1, grupo2, grupo3]
  #  shuffle(lista)
 #   print(f'A ordem da apresetação é : {lista}')

#programa principal
#lista = []
#print('Sorteio')
#grupo1 = str(input('1º Grupo :  '))
#grupo2 = str(input('2º Grupo :  '))
#grupo3 = str(input('3º Grupo :  '))
#sorteio(lista)

#def função():
    #n1 = 4
    #print(f'n1 dentro vale {n1}')


#n1 = 2
#função()
#print(f'n1 fora vale {n1}')

#def teste():
    #x = 8
    #print(f'Na função teste X ele vale {x}')

#PRINCIPAL
#n = 2
#print(f'Na variável N ele vale {n}')
#teste()

def par(n=0):
    if n % 2 == 0:
        return True
    else:
        return False


num = int(input('Digite um número : '))
if par(num):
    print('Número par !')
else:
    print('Número ímpar !')