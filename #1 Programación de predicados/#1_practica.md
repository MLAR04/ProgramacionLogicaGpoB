# Guardar este contenido en un archivo llamado Practica_Banco.md
contenido_md = """
# Práctica: Consultas sobre el Banco

## Objetivo
El objetivo de esta práctica es crear funciones en Python que permitan consultar la información de un diccionario llamado `Banco`, que simula la base de datos de clientes y transacciones. La práctica permite:  

- Verificar la edad de un cliente.  
- Consultar la raza de un cliente.  
- Consultar los servicios de préstamo del banco.  
- Verificar el estado de cuenta de un cliente.  
- Consultar operaciones económicas entre clientes y el banco.  
- Consultar los datos específicos de un cliente llamado "Osvaldo".

---

## Estructura del diccionario `Banco`

```python
Banco = {
    "Pedro": ["mayor de edad","30 años","Humano"],
    "inBanco": ["Tiene dinero","Presta dinero","500 dolares"],
    "cuenta": ["Tiene dinero","tiene cuenta"],
    "pedro": ["tiene dinero","no debe"],
    "osvaldo": ["recibio dinero", "tiene 1000 pesos"]
}

edad("mayor de edad", "30 años")
# Output: Pedro es mayor de edad y tiene 30 años

raza("Humano")
# Output: Pedro es Humano

Prestamo("Tiene dinero", "Presta dinero")
# Output: El banco sí Presta dinero

estado_cuenta("tiene dinero")
# Output: tiene dinero

ecomomia("tiene dinero", "no debe")
# Output: tiene dinero además no debe

osvaldo("recibio dinero", "tiene 1000 pesos")
# Output: Osvaldo tiene recibio dinero y tiene 1000 pesos

osvaldo("recibio dinero")
# Output: Osvaldo recibio dinero
