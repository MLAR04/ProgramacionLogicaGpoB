enfermedades = {
    "Gripe" : {"tos", "dolor de cabeza"},
    "Covid" : { "fiebre", "tos", "cansancio", "perdida del olfato"},
    "Migraña" : {"dolor de cabeza", "nauseas"},
    "Resfriado": {"congestion nasal", "fiebre", "tos"}
}

print("-- Sistema de diagostico de enfermedades comunes --")
print("Escriba sus sintomas: ", {s for sintomas in enfermedades.values() for s in sintomas})
print("Escribe tus sintomas separados por una coma.")

entrada = input("¿Cuáles son tus sintomas?: ")
sintomas_usuario = {s.strip().lower() for s in entrada.split(",")}

enfermedades_lower = {enf: {s.lower() for s in sintomas} for enf, sintomas in enfermedades.items()}

diagnostico = None

for enfermedad, sintomas in enfermedades_lower.items():
    if sintomas_usuario == sintomas:
        diagnostico = enfermedad
        break

if diagnostico:
    print(f"Su diagnostico es:{diagnostico}." )
else:
    print("No se puede diagnosticar")

