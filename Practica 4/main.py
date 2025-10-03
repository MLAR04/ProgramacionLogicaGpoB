
from funciones import diagnosticar

def main():
    print("=== Sistema de detección de enfermedades comunes ===")
    print("Síntomas posibles: tos, dolor de cabeza, fiebre, cansancio, perdida del olfato, nauseas, congestion nasal")
    print("Responde con síntomas separados por coma.\n")

    entrada = input(" Qué síntomas tienes?: ")
    sintomas_usuario = entrada.split(",")  

    resultado = diagnosticar(sintomas_usuario)
    print(f"\nDiagnóstico: {resultado}")

if __name__ == "__main__":
    main()
