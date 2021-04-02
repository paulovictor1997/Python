#pessoa = {'nome': 'Paulo', 'sexo': 'M', 'idade':23}
#pessoa['peso'] = 70.5
#for k, v in pessoa.items():
 #    print(f'{k} = {v}')

#print(f'O nome dele é {pessoa["nome"]} e a sua idade é {pessoa["idade"]}')

#brasil = []
#estado = {'UF': 'Alagoas','Capital': 'Maceió'}
#estado1 = {'UF': 'Pernambuco','Capital': 'Recife'}
#brasil.append(estado)
#brasil.append(estado1)
#print(brasil[0])

estado = {}
brasil = []
for c in range(0,3):
     estado['UF'] = str(input('Unidade Federativa : '))
     estado['Sigla'] = str(input('Sigla : '))
     brasil.append(estado.copy())
for e in brasil:
    for k, v in e.items():
        print(f'O campo {k} tem o valor {v}.')