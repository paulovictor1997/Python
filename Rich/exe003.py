from rich import print
from rich.table import Table    

tabela = Table(title="Tabela de preços")

tabela.add_column(header="Nome",justify="center")
tabela.add_column(header="Preço",justify="center")
tabela.add_row("Lápis","R$1.50",)
tabela.add_row("Borracha","R$1.50")

print(tabela)