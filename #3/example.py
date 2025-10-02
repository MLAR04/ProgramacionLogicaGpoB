#crear un diccionario con los nombres de los meses y la cantidad de días que tiene cada uno.
meses = {
    "Enero": 31,
    "Febrero": 28,
    "Marzo": 31,
    "Abril": 30,
    "Mayo": 31,
    "Junio": 30,
    "Julio": 31,    
    "Agosto": 31,
    "Septiembre": 30,
    "Octubre": 31,
    "Noviembre": 30,
    "Diciembre": 31
}
#generar 2 reglas lógicas:
#Regla 1: Un mes tiene 30 días si su nombre termina en "bre 
#Regla 2: Un mes tiene 31 días si su nombre no termina en "bre"

#generar sus dichos resultados y una tabla de verdad para cada una de ellas.

def verificar_dias_mes(mes: str):
    if mes not in meses:
        print("Mes no válido. Por favor, ingresa un mes correcto.")
        return

    dias = meses[mes]
    R1 = mes.endswith("bre") and dias == 30
    R2 = not mes.endswith("bre") and dias == 31

    print(f"\nRESULTADOS PARA EL MES INGRESADO ({mes}):")
    print(f"Días: {dias}")
    print(f"Regla 1 (termina en 'bre' y tiene 30 días): {R1}")
    print(f"Regla 2 (no termina en 'bre' y tiene 31 días): {R2}")

    print("\nTABLA DE VERDAD")
    print(f"{'Mes':<12}{'Días':<6}{'R1':<6}{'R2':<6}")
    print("-" * 30)
    for m, d in meses.items():
        r1 = m.endswith("bre") and d == 30
        r2 = not m.endswith("bre") and d == 31
        print(f"{m:<12}{d:<6}{str(r1):<6}{str(r2):<6}")

def main():
    mes = input("Ingresa el nombre de un mes (con la primera letra en mayúscula): ")
    verificar_dias_mes(mes)

if __name__ == "__main__":
    main()
    