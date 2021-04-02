frase = str(input('Digite a sua frase : ')).strip().upper()
palavra = frase.strip()#nessas etapas, ele dividiu já colocou ela toda em maiúscula para não complicar na comparação
junto = ''.join(palavra) #pega todas as palavras da frase e junta já com os espaços eliminados
inverso = ''
for letra in range(len(junto) -1, -1, -1) : #aqui ele está contando a frase de tràs para a frente na lista, voltando de uma em uma letra
    inverso += junto[letra]
if inverso == junto:
      print('TEMOS UM PALÍNDROMO ! ')
else:
      print('A PALAVRA NÃO É UM PALINDROMO')

      #macete, sem usar o for -  inverso = junto[::-1]