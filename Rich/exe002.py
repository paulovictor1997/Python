from rich import print
from rich.panel import Panel

caixa = Panel(renderable="Teste de painel de texto", title="Mensagem", style="blue")
print(caixa)