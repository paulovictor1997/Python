"""
Crie uma classe livro, que vai simular a passagem de páginas de um livro, considerando também,
se o usuário chegou ao fim da leitura. (VERSÃO NÃO FINALIZADA)
"""
from rich.console import Console
from rich.panel import Panel

console = Console()

class Livro : 
    def __init__(self,total_paginas):
        self.total_paginas = total_paginas
        self.pagina_atual = 1

    def mostrar_pagina(self):
        console.print(
            Panel.fit(
                f"[bold cyan]Página {self.pagina_atual}[/bold cyan]",
                title="Livro",
                border_style="blue"
            )
        )
    def proxima_pagina(self):
        if self.pagina_atual < self.total_paginas:
            self.pagina_atual += 1
            self.mostrar_pagina()
        else:
            console.print("[bold red]Você chegou ao fim do livro![/bold red]")

    def pagina_anterior(self):
        if self.pagina_atual > 1:
            self.pagina_atual -= 1
            self.mostrar_pagina()
        else:
            console.print("[bold yellow]Você já está na primeira página![/bold yellow]")
       
    def ir_para_pagina(self,numero):
        if 1 <= numero <= self.total_paginas:
            self.pagina_atual = numero
            self.mostrar_pagina()
        else:
          console.print(f"[bold red]Página {numero} não existe neste livro![/bold red]")


livro = Livro(10)
livro.mostrar_pagina()
livro.proxima_pagina()
livro.ir_para_pagina(10)
livro.ir_para_pagina(11)
livro.proxima_pagina()

#CHECAR A CORREÇÃO COM O  GUANABARA