print('-='*20)
print('Classificação Brasileirão 2020')
time = ('Atlético Mineiro', 'Vasco','Internacional','Bahia','Atlético Paranaense','Grêmio',
        'Atlético Goianiense','Santos','Fluminense','Sport','São Paulo',
        'Flamengo','Palmeiras','Botafogo','Bragantino','Corinthians',
        'Goias','Ceará','Fortaleza','Coritiba')
print('-='*20)
for c, pos in enumerate (time, +1):
    print(f'{c}º {pos}')
print('-='*20)
print(f'Classificados para a Libertadores : {time[0:4]}',end='\n')
print('-='*20)
print(f'Rebaixados para a série B : {time[-4:]}')
