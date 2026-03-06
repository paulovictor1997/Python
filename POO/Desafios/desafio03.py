"""
Crie a classe churrasco, onde seja possível informar quantas pessoas vão participar e mostre 
quanto de carne deve ser comprado, o custo total do churrasco e no final o preço por pessoa. 

"""
# Criando valores fixos para facilitar o exercicio
# 400g de carne por pessoa (0,4 kg) / Preço do kg da carne: R$ 82,40
from rich import print
from rich.panel import Panel

class Churrasco : 
        #Atributo de classe 
        consumo:float = 0.4
        preco_kg = 82.40

        def __init__(self, titulo, quant):
        #Atributo de instância
            self.titulo = titulo
            self.praticipantes = quant

        def __str__(self):
            return  f"Esse é o {self.titulo} com {self.praticipantes} pessoas participando !"
        
        #Métodos de calculo
        def calcular_quant_carne(self) -> float:
            return self.praticipantes * Churrasco.consumo

        def calcular_custo_total(self) -> float:
            return self.calcular_quant_carne() * self.preco_kg
        
        def custoIdividual(self) -> float:
            return self.calcular_custo_total() / self.praticipantes
        
        def analisar (self):
            conteudo = f"Analisando [green]{self.titulo}[/] com [blue]{self.praticipantes} convidados[/]."
            conteudo += f"\nCada participante comerá {Churrasco.consumo}KG e cada KG custa R${Churrasco.preco_kg:.2f}"
            conteudo += f"Recomendo comprar [blue]{self.calcular_quant_carne():.3f}[/] KG de carne."
            conteudo += f"\nO custo total é de : [yellow] R$ {self.calcular_custo_total():.2f} [/]"
            conteudo += f"\nCada pessoa pagará  :[yellow] R${self.custoIdividual():.2f} [/]"
            painel = Panel(conteudo, title=self.titulo)
            print(painel)
    

c = Churrasco(titulo="Churrasco dos amigos", quant=15)
c.analisar()