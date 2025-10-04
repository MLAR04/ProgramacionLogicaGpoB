from enfermedades_dict import enfermedades

def diagnosticar(consulta: list, enfermedades: dict) -> str:
    conjunto_consulta = set(consulta)
    for enfermedad, sintomas in enfermedades.items():
        if sintomas.issubset(conjunto_consulta):
            return f"Usted tiene {enfermedad}"
    return "No es posible diagnosticar una enfermedad con los sintomas proporcionados"


if __name__ == "__main__":
    input = input("Ingresa tus sintomas separados por una coma (e.g: tos, fiebre):")
    consulta = [sintoma.strip() for sintoma in input.split(',')]
    print(diagnosticar(consulta, enfermedades))