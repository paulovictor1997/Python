from time import sleep
def maior(* num):
    tam = len(num)
    print('Analisando os valores...')
    for valor in num:
        print(valor,end=' ')
        sleep(1)
    print(f'Foi citado {tam} valores')
    print(f'O maior valor informado foi {max(num)}')
    print('-'*30)


maior(1,3,5,9)
maior(7,11,12)
maior(10,20,40,100)
