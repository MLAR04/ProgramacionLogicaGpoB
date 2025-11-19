# Importar librerías necesarias
from sklearn.datasets import load_wine
from sklearn.tree import DecisionTreeClassifier, export_text
from sklearn.model_selection import train_test_split

# Cargar el dataset del vino
wine = load_wine()
X, y = wine.data, wine.target

# Dividir los datos en entrenamiento (80%) y prueba (20%)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Crear y entrenar el clasificador de árbol de decisión
# max_depth=2 permite reglas más interpretables
clf = DecisionTreeClassifier(max_depth=2, random_state=42)
clf.fit(X_train, y_train)

# Exportar y visualizar las reglas del árbol
rules = export_text(clf, feature_names=wine.feature_names)
print("Reglas del arbol de decision:")
print(rules)

# Evaluar precisión en los datos de prueba
accuracy = clf.score(X_test, y_test)
print(f"Precision del modelo en datos de prueba: {accuracy:.2f}")

# Punto adicional: probar otras profundidades (ejemplo)
if __name__ == "__main__":
    print("\nProbando sin limite de profundidad...")
    clf_full = DecisionTreeClassifier(max_depth=None, random_state=42)
    clf_full.fit(X_train, y_train)
    rules_full = export_text(clf_full, feature_names=wine.feature_names)
    print(rules_full)
    print("Precision sin limite:", clf_full.score(X_test, y_test))


