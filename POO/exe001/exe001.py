#DECLARAÇÃO DE CLASSE
class Pessoa :
    def __init__(self) : #Método construtor
        #Atributos de instância
        self.nome = ""
        self.idade = 0

    #Métodos de instância
    def aniversario(self):
        self.idade += 1

    def mensagem(self):
        return f"Me chamo {self.nome} e tenho {self.idade} anos !"

#DECLARAÇÃO DE OBJETOS - Chamando o método construtor
pessoa1 = Pessoa()
pessoa1.nome = "Paulo Victor"
pessoa1.idade = 28
pessoa1.aniversario()
print(pessoa1.mensagem())

print("-----------------------------")

pessoa2 = Pessoa()
pessoa2.nome = "Aleatório"
pessoa2.idade = 20
print(pessoa2.mensagem())