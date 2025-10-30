from hechos import recetas, proteinas

def proteina_animal(ingrediente):
    return ingrediente in proteinas.get("Animal", [])

def lacteos(receta):
    return "lacteo" in recetas[receta]["ingredientes"]

def huevos(receta):
    return "Huevo" in recetas[receta]["ingredientes"].get("proteina", {})

def miel(receta):
    return "Miel" in recetas[receta]["ingredientes"].get("condimento", {})

def vegetariana(receta):
    proteinas_receta = list(recetas[receta]["ingredientes"].get("proteina", {}).keys())
    for proteina in proteinas_receta:
        if proteina_animal(proteina):
            return False
    return True

# Regla 1 "Si una receta es vegetariana y no incluye láceteos, huevos o miesl ENTONCES es vegana."
def regla_es_vegana(receta):
    return (vegetariana(receta) and 
            not lacteos(receta) and 
            not huevos(receta) and 
            not miel(receta))

# Regla 2: "SI una receta cumple con el 75% de VERDURAS, CARBOHIDRATOS Y PROTEINAS seleccionadas ENTONCES se muestra."
def cumple_porcentaje(receta, ingredientes_usuario, umbral=75):
    ingredientes_totales = 0
    coincidentes = 0
    
    for categoria in ["carbohidrato", "verdura", "proteina"]:
        ingredientes_cat = recetas[receta]["ingredientes"].get(categoria, {})
        ingredientes_totales += len(ingredientes_cat)
        for ingrediente in ingredientes_usuario:
            if ingrediente in ingredientes_cat:
                coincidentes += 1
    
    return (coincidentes / ingredientes_totales * 100) >= umbral if ingredientes_totales > 0 else False

def resolver_recetas_aptas(ingredientes_usuario):
    return [receta for receta in recetas 
            if cumple_porcentaje(receta, ingredientes_usuario)]

def main():
    ingredientes_usuario = ["cerdo", "tortilla_de_maiz", "cebolla", "cilantro", "piña", "flor_calabaza"]
    
    # Encontrar recetas que coinciden con el 75% de ingredientes
    recetas_aptas = resolver_recetas_aptas(ingredientes_usuario)
    print(f"Recetas que cumplen: {recetas_aptas}")
    
    # Verificar si una receta es vegana
    for receta in recetas_aptas:
        es_vegana = regla_es_vegana(receta)
        print(f"Los {receta} es vegana? {es_vegana}")

if __name__ == "__main__":
    main()