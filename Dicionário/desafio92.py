from datetime import datetime
dados = {}
dados ['nome'] = str(input('Nome : '))
nascimento = int(input('Ano de nascimento : '))
dados['idade'] = datetime.now().year - nascimento
dados['ctps'] = int(input('Carteira de trabalho (Se não tiver, digite 0 ): '))
if dados['ctps'] !=0:
    dados['contrato'] = int(input('Ano de contratação : '))
    dados['salário'] = float(input('Salário : '))
    dados['aposentadoria'] = dados['idade'] + ((dados['contrato'] + 35) - datetime.now().year)
print('-='*30)
for k,v in dados.items():
    print(f' - {k} tem o valor {v}')