"""
Crie a classe churrasco, onde seja possível informar quantas pessoas vão participar e mostre 
quanto de carne deve ser comprado, o custo total do churrasco e no final o preço por pessoa. 

"""
# Criando valores fixos para facilitar o exercicio
# 400g de carne por pessoa (0,4 kg) / Preço do kg da carne: R$ 50,00

class Churrasco : 
    def __init__(self, qtd_pessoas):
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
        print(f"Quantidade de pessoas : {self.qtd_pessoas}")
        print(f"Carne necessária : {self.calcular_carne():.2f} KG")
        print(f"Custo total : R$ {self.custo_total():.2f}")
        print(f"Valor por pessoa : R$ {self.calculo_por_pessoa():.2f}")


churrasco = Churrasco(10)
churrasco.resumo()