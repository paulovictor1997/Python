"""
Desafio 16 - 
Crie uma classe funcionário, onde pode cadastrar nome, setor e cargo, criar também
um método que permite ao funcionário se apresentar.
"""
from rich import print

class Funcionario :
    def __init__(self, nome, setor, cargo):
        self.nome = nome
        self.setor = setor
        self.cargo = cargo
    
    def apresentar(self):
        print(f"Olá, meu nome é [bold blue]{self.nome}[/bold blue] e trabalho no setor de {self.setor} como [bold blue]{self.cargo}[/bold blue]")
    

funcionario = Funcionario("Paulo", "Tecnologia", "Desenvoldor")
funcionario.apresentar()

print("-----------------------------")

funcionario2 = Funcionario("Victor", "Tecnologia", "Redes")
funcionario2.apresentar()
