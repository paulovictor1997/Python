"""
Crie uma classe livro, que vai simular a passagem de páginas de um livro, considerando também,
se o usuário chegou ao fim da leitura. (VERSÃO FINALIZADA)
"""
from rich import print
import time

class Livro : 
    def __init__(self, titulo, paginas):
        self.titulo = titulo
        self.total_paginas = paginas
        self.pagina_atual = 1 #Página atual sempre começará com 1

        print(f":open_book:[blue] Você acabou de abrir o livro [red]{self.titulo}[/] tem {self.total_paginas} páginas no total. Você agora está ná página {self.pagina_atual}[/]")

    def avancar_paginas(self, qtd = 1):
        cont = 0
        for pg in range(0, qtd, 1):
            if not self.fim_do_livro():
                self.pagina_atual +=1
                print(f"Pág {self.pagina_atual} :arrow_forward:", end="")
                time.sleep(0.2)
                cont+=1
        print(f"[blue]Você avançou {cont} páginas e agora está na pagina {self.pagina_atual}[/blue]")
        if self.fim_do_livro():
            print(":closed_book: [red]Você chegou ao fim do livro[/red]")
        
    def fim_do_livro(self):
        if self.pagina_atual == self.total_paginas:
            return True
        else:
            return False
        


l1 = Livro(titulo="Engenharia de Software",paginas=20)
l1.avancar_paginas(5)
l1.avancar_paginas(10)
l1.avancar_paginas(50) #teste passando do limites de página.
