"""
Crie uma classe caneta, que simule uma caneta colorida podendo escrever frases em cores relativas. 
(CONFERIR COM A VERSÃO DO GUANABARA)
"""
from rich.console import Console
from rich.panel import Panel
from rich.align import Align

console = Console()

class Caneta :
    def __init__(self,cor): #atributo
        if not cor:
            raise ValueError("A caneta precisa ter uma cor.")
        self.cor = cor.lower()

    def escrever(self,frase):
        if not frase:
            raise ValueError("A frase não pode estar vazia")
        texto_colorido = f"[bold {self.cor}]{frase}[/bold {self.cor}]"

        painel = Panel.fit(
            Align.center(texto_colorido),
            title=f"Caneta {self.cor.capitalize()}",
            border_style=self.cor
        )

        console.print(painel)

#Métodos
try:
    cor_da_caneta = Caneta("red")
    cor_da_caneta.escrever("A frase colorida fica assim")
except ValueError as erro:
    console.print(f"[bold red]Erro:[/bold red] {erro}")