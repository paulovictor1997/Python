"""
Crie uma classe caneta, que simule uma caneta colorida podendo escrever frases em cores relativas. 
(VERSÃO FINALIZADA)
"""
from rich import print

class Caneta :
    def __init__(self, cor = "azul"):
        escolha = ""
        match cor.lower().strip():
            case "azul":
                escolha = "[blue]"
            case "vermelho" | "vermelha":
                escolha = "[red]"
            case "verde":
                escolha = "[green]"
            case _:  #Se ele colocar uma cor que não exista, ficará com o branco.
                escolha = "[white]"
        self.cor = escolha
        self.tampada = True

    def escrever (self,msg):
        if self.tampada :
            print(f":prohibited: A {self.cor} caneta [/] está tampada!")
        else:   
            print(f"{self.cor}{msg}[/]", end="")

    def quebrar_linha(self,qtd = 1):
        pass   

    def tampar(self):
        self.tampada = True

    def destampar(self):
        self.tampada = False




c1 = Caneta("azul")
c2 = Caneta("vermelha")
c3 = Caneta("verde")

c1.destampar()
c2.destampar()

c1.escrever("Olá, mundo")
c2.escrever("Está funcionando")
c3.escrever("Está dando certo")