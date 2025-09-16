

# ==========================
# Main: ejecuta todos los ejercicios
# ==========================

import suma
import factorial
import fibonacci
import lista

if __name__ == "__main__":
    print("=== Ejercicio: suma ===")
    print("suma(3, 5) =", suma.suma(3, 5))
    
    print("\n=== Ejercicio: factorial ===")
    print("factorial(5) =", factorial.factorial(5))
    
    print("\n=== Ejercicio: fibonacci ===")
    print("Primeros 10 números de Fibonacci:")
    for i in range(10):
        print(fibonacci.fibonacci(i), end=" ")
    print()
    
    print("\n=== Ejercicio: lista con map, filter y reduce ===")
    print("Cuadrados:", lista.cuadrados)
    print("Pares:", lista.pares)
    print("Suma de [1..10]:", lista.suma_total)
    print("Producto de [1..5]:", lista.factorial)
