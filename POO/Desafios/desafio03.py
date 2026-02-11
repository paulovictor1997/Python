"""
Crie a classe churrasco, onde seja possível informar quantas pessoas vão participar e mostre 
quanto de carne deve ser comprado, o custo total do churrasco e no final o preço por pessoa. 

"""
# Criando valores fixos para facilitar o exercicio
# 400g de carne por pessoa (0,4 kg) / Preço do kg da carne: R$ 50,00
from rich import print

class Churrasco : 
    def __init__(self, qtd_pessoas):
        if qtd_pessoas <=0: 
            raise ValueError ("Adicione ao menos uma pessoa") #Caso passe o número zerado de pessoas, o código irá mostrar esse erro
        self.qtd_pessoas = qtd_pessoas
        self.consumo_por_pessoa = 0.4 
        self.preco_kg = 50.0
    
    def calcular_carne(self):
        return self.qtd_pessoas * self.consumo_por_pessoa
    
    def custo_total(self):
        return self.calcular_carne() * self.preco_kg
    
    def calculo_por_pessoa(self):
        return self.custo_total() / self.qtd_pessoas
    
    def resumo(self):
        print("=== Churrasco ===")
        print(f"Quantidade de pessoas :[blue]{self.qtd_pessoas}[/blue]")
        print(f"Carne necessária : [blue] {self.calcular_carne():.2f} KG[/blue]")
        print(f"Custo total : [blue] R$ {self.custo_total():.2f}[/blue]")
        print(f"Valor por pessoa : [blue] R$ {self.calculo_por_pessoa():.2f}[/blue]")
try:
    churrasco = Churrasco(10)  
    churrasco.resumo()
except ValueError as erro:
    print("=" * 40)
    print("[bold red]ERRO NO CHURRASCO[/bold red]")
    print(f"Motivo: {erro}")
    print("=" * 40)

#churrasco = Churrasco(10) 
#churrasco.resumo()