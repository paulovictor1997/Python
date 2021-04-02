def notas(*n,geral = False):
    g = {}
    g["total"] = len(n)
    g["maior"] = max(n)
    g["menor"] = min(n)
    g['média'] = sum(n)/len(n)
    if geral:
        if g['média'] >= 6:
            g['situação'] = 'APROVADO'
        elif g['média'] < 6:
            g['situação'] = 'RECUPERAÇÃO'

    return g

#resposta = notas(5.5,5.0,6.0,geral=True)
#print(resposta)
n1 = float(input('Digite a primeira nota : '))
n2 = float(input('Digite a segunda nota  : '))
print(notas(n1,n2,geral=True))