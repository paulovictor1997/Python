expressao = str(input('Digite a expressão : '))
pilha = []
for s in expressao:
    if s == '(':
        pilha.append('(')
    elif s == ')':
        if len(pilha) > 0 :
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Expressão válida !')
else:
    print('Expressão ínvalida !')