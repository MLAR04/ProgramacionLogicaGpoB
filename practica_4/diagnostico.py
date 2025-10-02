import json
from typing import List

def realizar_diagnostico(sintomas_paciente: List[int], nombres_enfermedades:List[str]) -> None:
    # Compara los síntomas del paciente con la matriz de diagnóstico para encontrar una coincidencia.
    enfermedad_diagnosticada = None
    for i, perfil_enfermedad in enumerate(diagnostico):
        if sintomas_paciente == perfil_enfermedad:
            enfermedad_diagnosticada = nombres_enfermedades[i]
            break
    if enfermedad_diagnosticada:
        print(f"El diagnostico es: {enfermedad_diagnosticada}")
    else:
        print("No se pudo determinar la enfermedad con los sintomas proporcionados.")

def iniciar_diagnostico(lista_sintomas:List[str], nombres_enfermedades: List[str]) -> None:
    # Inicia el proceso de diagnóstico, preguntando al usuario sobre sus síntomas.

    sintomas_paciente = []
    print("Por favor, responda con y/n a las siguientes preguntas.")
    for sintoma in lista_sintomas:
        while True:
            respuesta = input(f"¿Usted tiene {sintoma}? (y/n): ").lower()
            if respuesta in ["y", "n"]:
                sintomas_paciente.append(1 if respuesta == "y" else 0)
                break
            else:
                print("Respuesta no valida. Por favor, solo responda con 'y' o 'n'.")
 
    realizar_diagnostico(sintomas_paciente, nombres_enfermedades)


if __name__ == "__main__":
    ## INICIALIZACIÓN DE VARIABLES
    # Matriz de diagnostico
    diagnostico = [   
    [0, 0, 1, 0, 0, 0, 1],  # Gripe
    [1, 0, 0, 1, 0, 1, 1],  # Covid
    [0, 0, 1, 0, 1, 0, 0],  # Migraña
    [0, 1, 0, 1, 0, 0, 1]   # Resfriado
 ]

with open("enfermedades.json", "r") as json_file:
    datos_enfermedades = json.load(json_file)
    nombres_enfermedades = list(datos_enfermedades["enfermedades"])
    lista_sintomas = datos_enfermedades["sintomas"]
    print("Bienvenido al sistema de diagnóstico de enfermedades.")
    iniciar_diagnostico(lista_sintomas, nombres_enfermedades)