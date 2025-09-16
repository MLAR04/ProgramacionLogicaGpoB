# Practica 2 - Programacion Funcional en Python


## Contenido de los ejercicios

### Ejercicio 1: Funcion suma
- Se desarrollo una funcion `suma(a, b)` que solo depende de sus parametros.
- El usuario ingresa dos numeros desde la terminal.
- La funcion devuelve la suma de ambos numeros.
- El resultado se muestra en pantalla de manera dinamica.

**Proceso:**
1. Se solicita al usuario ingresar dos numeros.
2. Se llama a la funcion `suma` pasando los numeros como parametros.
3. Se imprime el resultado.

---

### Ejercicio 2: Factorial recursivo
- Se implemento una funcion recursiva `factorial(n)` que calcula el factorial de un numero.
- El usuario ingresa un numero desde la terminal.
- La funcion devuelve el factorial calculado de manera recursiva.

**Proceso:**
1. Si el numero es 0 o 1, la funcion retorna 1 (caso base).
2. Si el numero es mayor, la funcion se llama a si misma con `n-1` y multiplica el resultado por `n`.
3. Se imprime el resultado final.

---

### Ejercicio 3: Fibonacci recursivo
- Se desarrollo una funcion recursiva `fibonacci(n)` que calcula la secuencia de Fibonacci hasta la posicion `n`.
- El usuario ingresa la posicion hasta la que desea ver la secuencia.
- La funcion devuelve una lista con todos los numeros de la secuencia hasta `n`.

**Proceso:**
1. Casos base: si n = 0 retorna [0], si n = 1 retorna [0,1].
2. Para n mayor, la funcion llama a fibonacci(n-1) y agrega el siguiente numero sumando los dos ultimos.
3. Se imprime la secuencia completa.

---

### Ejercicio 4: Operaciones con listas
- Se trabaja con la lista `[1,2,3,4,5,6,7,8,9,10]`.
- Se aplican funciones de orden superior `map`, `filter` y `reduce`.

**Detalles:**
1. **Cuadrados con map:**  
   - Se genera una nueva lista donde cada numero de la lista original se eleva al cuadrado usando `map` y una funcion lambda.
2. **Filtrar numeros pares con filter:**  
   - Se seleccionan solo los numeros pares de la lista usando `filter` y `x % 2 == 0`.
3. **Suma con reduce:**  
   - Se calcula la suma de todos los elementos de la lista usando `reduce` con una funcion lambda que suma dos elementos.
4. **Producto de los primeros 5 elementos con reduce:**  
   - Se toma una sublista con los primeros cinco elementos y se aplica `reduce` con multiplicacion para obtener el producto total.

**Proceso general:**
- `map` transforma cada elemento de la lista aplicando una funcion.
- `filter` selecciona elementos que cumplen una condicion.
- `reduce` combina elementos sucesivos de la lista en un unico resultado usando una funcion acumulativa.

---

## Uso
1. Cada ejercicio esta en un script independiente (`ejercicio1_suma.py`, `ejercicio2_factorial.py`, etc.).
2. Para ejecutar un ejercicio, abrir la terminal, ir a la carpeta `Practica2` y ejecutar:
