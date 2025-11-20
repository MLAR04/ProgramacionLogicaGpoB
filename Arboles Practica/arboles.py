import matplotlib.pyplot as plt  # Librería para gráficos
from sklearn.datasets import load_wine
from sklearn.tree import DecisionTreeClassifier, plot_tree # plot_tree es para dibujar
from sklearn.model_selection import train_test_split

def run_decision_tree_visual():
    #Cargar datos 
    wine = load_wine()
    X, y = wine.data, wine.target
    
    #Dividir entrenamiento y prueba 
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    #Entrenar modelo (max_depth=3 para que el gráfico se vea bien y no sea gigante)
    clf = DecisionTreeClassifier(max_depth=3, random_state=42)
    clf.fit(X_train, y_train)

    #Precision
    print(f"Precisión: {clf.score(X_test, y_test):.4f}")
    
    # Configurar el tamaño de la imagen
    plt.figure(figsize=(12, 8))
    
    # COSO para dibujar el árbol
    plot_tree(clf, 
              feature_names=wine.feature_names, 
              class_names=wine.target_names,   
              filled=True,                     
              rounded=True,                   
              fontsize=10)                     
    
    # Título y mostrar
    plt.title("Árbol de Decisión - Dataset Vinos")
    plt.show() # Esto abrirá ungráfico

if __name__ == "__main__":
    run_decision_tree_visual()