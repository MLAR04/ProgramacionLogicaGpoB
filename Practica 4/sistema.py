#ESTE SISTEMA SE VA A ENCARGAR DE DIAGNOSTICARLE UNA ENFERMEDAD A UN USUARIO EN 
#BASE A LOS SINTOMAS QUE EL INGRESE 

#VAMOS A IMPORTAR EL DICCIONARIO DESDE OTRO ARCHIVO 
from universo import enfermedades


#ESTO SERIA SI LO HACEMOS EN EL MISMO ARCHIVO, LO DEJE DE EJEMPLO
# LO PRIMERO QUE HACEMOS ES NUESTRO UNIVERSO 

""" enfermedades = {
                "gripa": {"tos", "dolor de cabeza"},
                "covid": {"fiebre", "tos", "cansancio", "perdida del olfato"},
                "migrana": {"dolor de cabeza", "nauseas"},
                "resfriado": {"congestion nasal", "fiebre", "tos" }
                } """
#YO ESTABA EQUIVOCADO E INTENTE HACERLO ASI PERO ME DABA ERRORES 
#sintomas[] = input("Ingrese sus sintomas")

#ASI SERIA LA MANERA CORRECTA:

# Pides los sintomas en una sola linea separados por comas
entrada = input("\n Ingresa tus sintomas separados por coma: ")

#lower convierte todo lo que ingresaste a minusculas para evitar errores
# Los conviertes en lista con split
#split hace un corte (lista) cada que detecte una coma
sintomas = entrada.lower().split(",")

# Les quitamos espacios al inicio y al final
sintomas = [s.strip() for s in sintomas]

print("Tus sintomas son:", sintomas)

# Convertimos la lista a conjunto para comparar mejor
sintomas_usuario = set(sintomas)

# Lista para guardar coincidencias
coincidencias = []

# Comparamos con las enfermedades
for enfermedad, sintomas_enf in enfermedades.items():
    # Si todos los sintomas del usuario estan dentro de los sintomas de la enfermedad
    if sintomas_usuario.issubset(sintomas_enf):
        coincidencias.append(enfermedad)

# Aplicamos las reglas
if len(coincidencias) == 1:
    print(f"Diagnostico: tienes {coincidencias[0]} \n")
elif len(coincidencias) > 1:
    print("Tus sintomas coinciden con varias enfermedades, no se puede diagnosticar con precision. \n")
else:
    print("No se encontro una enfermedad con esos sintomas. \n")
