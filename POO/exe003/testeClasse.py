class ContaBancaria:
    def __init__(self,id,nome,saldo=0):
        self.id = id
        self.titular = nome
        self.saldo = saldo

    def __str__(self):
        return f"A conta {self.id} de {self.titular} tem R${self.saldo:,.2f} de saldo."
    

c1 = ContaBancaria(id=112,nome="Paulo",saldo=3000)
print(c1)
