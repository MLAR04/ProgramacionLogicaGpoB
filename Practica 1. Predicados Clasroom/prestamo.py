# Hechos
prestamos = {
    "Brandon": ["hipotecario"]  # Brandon puede generar préstamos en efectivo (Le puse  de hipotecarios para hacer pruebas)
}

# Regla: Brandon necesita un deudor para otorgar préstamos
def requiere_deudor(nombre):
   return nombre in prestamos and len(prestamos[nombre]) > 0

# Consultas
print("¿Brandon hace préstamos de efectivo?", "efectivo" in prestamos.get("Brandon", []))  # Verdadera
print("¿Brandon hace préstamos hipotecarios?", "hipotecario" in prestamos.get("Brandon", []))  # Falsa

#EN ESTE CODIGO TENGO DUDAS PORQUE A PAPEL LO CONSIDERE UNA BUENA REGLA,
#PERO YA PROGRAMANDOLO, PARECE QUE PUEDE HACERSE CON PUROS PRINTS, 
#SIN NECESIDAD DE LA FUNCION