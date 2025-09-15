## Desarrollo Funcional en Python 

##### practica#2
 
Desarrolla en python los siguientes ejercicios:
(Nota: en la terminal, utiliza el sig comando para correr los scripts: "Python nombre del archivo.py")
1. (Suma de parametros no independientes) Desarrollar una funcion suma(a,b), la cual solo deba de depender de dichos parametros: 
La función recibe dos parametros (a,b), que al sumar los dan el resultado de un parametro R, y al final simplemte se imprime un mensaje que idica que numeros se sumaron y cual fue el resultado 

2. (función recursiva para factorial) Implementar  una función recursiva factorial(n) que calcule el factorial de un número:

la función recibe un parametro n, donde primero se verifica que número es. En el caso de que n sea igual a 0 ó sea igual a 1, la función regresará 1, pero si fuera caso contrario, regresa el valor n multiplicado por la fución factorial, pero que ahora recibe n-1. Al final, se imprime un mensaje, donde indique el número dado y su factorial.

3.(función recursiva para Fibonacci) Escribir una función recursiva que calcule el n-ésimo número de Fibonacci:
La función fibonacci_memo utiliza memoización, una técnica que almacena resultados previamente calculados en un diccionario para evitar repetir operaciones. Cuando se llama a la función, primero verifica si ya calculó ese número de Fibonacci; si está en el diccionario, lo devuelve inmediatamente. Si no, calcula recursivamente los dos números anteriores, guarda el resultado y lo retorna.

4. (listas con map, filter, etc): Dada la lista [1,2,3,4,5,6,7,8,9,10]:
-Genera una nueva lista con los cuadrados de cada número usando map.
-Filtra los números pares usando filter
-Usa reduce para calcular:
-La suma de [1..10]
-El producto [1..5]






