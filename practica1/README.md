### Pensando en un contexto financiero, utiliza la siguiente lista de predicados, por cada uno genera un Hecho, una Regla y 2 Consultas (una que resulte verdadera y una que resulte falsa).
- "X" es un cliente.
- "Y" e un banco.
- "X" tiene una cuenta en el banco "Y".
- "Y" puede generar un préstamo de tipo "W".
- "X" recibió un monto "Z" de dinero.

#### Ejercicio resuelto
- Hecho: Pedro es un cliente. 
Regla: Pedro está afiliado a un banco 
Consulta 1: Pedro tiene cuenta ?(verdadero) 
Consulta 2: María tiene cuenta? (Falso) 

- Hecho: BBVA es un banco. 
Regla: BBVA tiene clientes 
Consulta 1: Tiene clientes BBVA? (verdadero) 
Consulta 2: María es cliente de BBVA? (Falso) 

- Hecho: Pedro tiene una cuenta en el banco BBVA. 
Regla: Deben ser mayor de 18 para tener una cuenta. 
Consulta 1: Pedro es mayor de 18?(verdadero) 
Consulta 2: Pedro es menor de 18? (Falso) 

- Hecho: BBVA puede generar un prestamo de tipo hipotecario. 
Regla: El cliente necesita una casa para pedir el prestamo. 
Consulta 1: Juan tiene casa ?(verdadero) 
Consulta 2: BBVA tiene prestamos estudiantiles? (falso) 

- Hecho: Pedro recibió un monto 700,000 de dinero. 
Regla: los prestamos a partir de 500.000 se consideran altos. 
Consulta 1: Pedro recibió un prestamo alto? (verdadero) 
Consulta 2: Pedro recibió 100,000? (Falso) 
