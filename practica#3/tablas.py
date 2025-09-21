from rich.console import Console
from rich.table import Table
from itertools import product
from typing import Callable

def generar_tabla_verdad(nombre: str, funcion: Callable, nombres_parametros: list[str]):
    console = Console()
    table = Table(title=f"Tabla de Verdad: {nombre}", show_lines=True)

    for nombre_parametro in nombres_parametros:
        table.add_column(nombre_parametro, justify="center")
    table.add_column("Resultado", justify="center", style="bold green")

    for valores in product([False, True], repeat=len(nombres_parametros)):
        # Extraer valores/datos individuales
        resultado = funcion(*valores)
        fila = [*map(str, valores), str(resultado)]
        table.add_row(*fila)

    console.print(table)
