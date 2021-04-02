time = ('Atlético Mineiro', 'Vasco','Internacional','Bahia','Atlético Paranaense','Grêmio',
        'Atlético Goianiense','Santos','Fluminense','Sport','São Paulo',
        'Flamengo','Palmeiras','Botafogo','Bragantino','Corinthians',
        'Goias','Ceará','Fortaleza','Coritiba')
print(f'Tabela Brasileirão 2020 : {time}')
print('-='*20)
print(f'Os 5 primeiros na classificação são : {time [0:6] }')
print('-='*20)
print(f'Os 4 últimos são : {time [16:21]}')
print('-='*20)
print(f'Os times em ordem alfabética : {(sorted(time))}')
print('-='*20)
print(f'O time do Santos está na {time.index("Santos") + 1} posição') #Index vai me mostrar especificamente a posição na tupla
