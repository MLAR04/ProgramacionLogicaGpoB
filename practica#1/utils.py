from rich.console import Console
from rich.table import Table

console = Console()

def mostrar_tabla(titulo: str, consultas: list[tuple[str, bool]]) -> None:
    tabla = Table(title=titulo)
    tabla.add_column("Consulta", style="cyan")
    tabla.add_column("Resultado", style="bold green")

    for texto, resultado in consultas:
        tabla.add_row(texto, str(resultado))

    console.print(tabla)