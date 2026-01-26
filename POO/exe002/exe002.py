#MELHORANDO O CÓDIGO ANTERIOR
class Pessoa :
    def __init__(self, name = "vazio", age = 0) : #Método construtor
        #Atributos de instância
        self.nome = name
        self.idade = age

    #Métodos de instância
    def aniversario(self):
        self.idade += 1

    def mensagem(self):
        return f"Me chamo {self.nome} e tenho {self.idade} anos !"

#DECLARAÇÃO DE OBJETOS - Chamando o método construtor
pessoa1 = Pessoa(name="Paulo Victor", age=28)
pessoa1.aniversario()
print(pessoa1.mensagem())

print("========================")
pessoa1 = Pessoa(name="João", age=27)
print(pessoa1.mensagem())