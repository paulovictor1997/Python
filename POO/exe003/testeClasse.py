class ContaBancaria:
    """
    Docstring para ContaBancaria
    Criação de um objeto de conta bancária
    """
    def __init__(self,id,nome,saldo=0):
        self.id = id
        self.titular = nome
        self.saldo = saldo

    def __str__(self):
        return f"A conta {self.id} de {self.titular} tem R${self.saldo:,.2f} de saldo."
    
    def depositar(self,valor):

        self.saldo += valor
        print(f"Deposito de R${valor:,.2f} na conta {self.id} autorizado")
    
    def sacar(self,valor):
        if valor > self.saldo:
            print(f"Saque NEGADO de valor R${valor:,.2f} na conta {self.id}. SALDO INSUFICIENTE")
        else :
            self.saldo -= valor
            print(f"Saque no valor de R${valor:,.2f} na conta {self.id}")
    
    

c1 = ContaBancaria(id=112,nome="Paulo",saldo=3000)
c1.depositar(500)
c1.sacar(2000)
print(c1)

