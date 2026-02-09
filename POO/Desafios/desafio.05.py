from rich import print
from rich.table import Table    

class Gamer:
    # Atributos
    def __init__(self, nome, nick, fav_games):
        self.nome = nome
        self.nick = nick
        self.fav_games = fav_games

    def ficha(self):
        table = Table(title="Ficha do Gamer")

        table.add_column("Nome", justify="center", style="blue", no_wrap=True)
        table.add_column("Nick", justify="center", style="red")
        table.add_column("Games favoritos", justify="left", style="green")

        # transforma a lista de jogos em texto
        # fav_games receberá mais de um jogo, então é formatado como uma lista.
        jogos_formatados = "\n".join(self.fav_games)

        # adiciona UMA linha à tabela
        table.add_row(
            self.nome,
            self.nick,
            jogos_formatados
        )

        print(table)

# Métodos
gamer1 = Gamer("Paulo","Paulo97",["Mortal Kombat", "God of War", "Call of Duty"])
gamer1.ficha()
