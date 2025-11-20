# arbol_decision.py
from sklearn.datasets import load_wine
from sklearn.tree import DecisionTreeClassifier, export_text
from sklearn.model_selection import train_test_split

def entrenar_arbol(max_depth=None):
    # Cargar los datos
    wine = load_wine()
    X, y = wine.data, wine.target

    # Dividir en entrenamiento y prueba
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    # Entrenar clasificador
    tree = DecisionTreeClassifier(max_depth=max_depth, random_state=42)
    tree.fit(X_train, y_train)

    # Exportar reglas
    rules = export_text(tree, feature_names=wine.feature_names)

    # Exactitud del modelo
    precision = tree.score(X_test, y_test)

    return rules, precision

def main():
    print("\n=== Árbol con profundidad limitada (max_depth=2) ===")
    rules_limited, precision_limited = entrenar_arbol(max_depth=2)
    print(rules_limited)
    print("Precisión:", precision_limited)

    print("\n=== Árbol sin límite de profundidad (max_depth=None) ===")
    rules_full, precision_full = entrenar_arbol(max_depth=None)
    print(rules_full)
    print("Precisión:", precision_full)

if __name__ == "__main__":
    main()
