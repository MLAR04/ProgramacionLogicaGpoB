from sklearn.datasets import load_wine
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
import random
import csv
import os

def wine_tree(x, y):
    rs = random.randint(1, 99)
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=rs)
    
    tree = DecisionTreeClassifier(max_depth=None, random_state=rs)
    tree.fit(x_train, y_train)
    
    precision = tree.score(x_test, y_test)
    return precision * 100

def ajustar_csv(iteracion, result):
    nombre_archivo = 'resultados_wine.csv'
    archivo_existe = os.path.isfile(nombre_archivo)
    
    with open(nombre_archivo, mode='a', newline='') as file:
        writer = csv.writer(file)
        if not archivo_existe:
            writer.writerow(['Iteracion', 'Precision']) # Encabezados
        writer.writerow([iteracion, round(result, 2)])

def analizar_resultados():
    valores = []
    try:
        with open('resultados_wine.csv', mode='r') as file:
            reader = csv.reader(file)
            next(reader)
            
            for row in reader:
                valores.append(float(row[1]))
        
        if valores:
            promedio = sum(valores) / len(valores)
            maximo = max(valores)
            minimo = min(valores)

            print("\n" + "="*30)
            print(" RESUMEN DE RESULTADOS")
            print("="*30)
            print(f"Muestras totales : {len(valores)}")
            print(f"Precisión Máxima : {maximo:.2f} %")
            print(f"Precisión Mínima : {minimo:.2f} %")
            print(f"Promedio Total   : {promedio:.2f} %")
            print("="*30)
        else:
            print("El archivo CSV está vacío.")

    except FileNotFoundError:
        print("No se encontró el archivo CSV para analizar.")

# Main
if __name__ == "__main__": 
    wine = load_wine()
    
    if os.path.exists('resultados_wine.csv'):
        os.remove('resultados_wine.csv')

    print("Generando datos...")
    for i in range(50):
        result = wine_tree(wine.data, wine.target)
        ajustar_csv(i, result)
    
    print("Proceso de guardado terminado.")
    
    analizar_resultados()