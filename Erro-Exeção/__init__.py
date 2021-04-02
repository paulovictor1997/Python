try:
    a = int(input('Numerador : '))
    b = int(input('Denominador : '))
    d = a/b
except ZeroDivisionError:
    print('Tivemos um problema, o denominador não pode ser zero !')
except ValueError:
    print('Só é aceito que se digite números inteiros')
else:
    print(f'Resultado da divisão : {d:.1f}')
finally:
    print('VOLTE SEMPRE !')