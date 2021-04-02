def area(largura, comprimento):
  area = largura * comprimento
  print(f'A área do terreno {largura} X {comprimento} é de : {area}m²  ')

print('Controle de Terreno')
print('-'*20)
largura = float(input('Largura (m) : '))
comprimento = float(input('Comprimento (m) : '))
area(largura,comprimento)

