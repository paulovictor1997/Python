"""
Crie uma classe Produto, onde podemos cadastrar nome e o preço. Crie também um método que mostre
etiqueta de preço do produto.
"""

from rich.console import Console
from rich.panel import Panel
from rich.align import Align
from rich import box

console = Console()
#Atributos
class Produto:
    def __init__(self,nome,preco):
       if preco <= 0:
            raise ValueError("O preço deve ser maior que zero.")

       self.nome = nome
       self.preco = preco
    
    def etiqueta(self):
        content = f"[blue]{self.nome}[/blue] - [green]R$ {self.preco:.2f}[/green]"

        painel = Panel(
            Align.center(content),
            title= "Etiqueta",
            border_style="yellow",
            width=40,
        )

        console.print(painel)

#Conteúdo principal
try:
    #Métodos
    produto = Produto("Notebook Gamer",4500)
    produto.etiqueta()
    print("="*40)
    produto2 = Produto("Computador", 5000)
    produto2.etiqueta()
except ValueError as erro:
    console.print(f"[bold red]Erro:[/bold red] {erro}")
