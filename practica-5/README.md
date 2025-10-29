### Equipo EDUCACION

## Temas, Subtemas y preguntas
Para esta practica estoy utilizando de nuestra base de conocimientos los temas, subtemas, preguntas y respuestas declaradas


## Clausulas de Horn
Una pregunta X es del tema Y si existe un subtema Z tal que la pregunta X pertenece al subtema Z y el subtema Z pertenece al tema Y.

pregunta_es_del_tema(X, Y) :- pregunta(Z, X), subtema(Y, Z)

Una respuesta R es correcta para la pregunta P si R es igual a la respuesta correcta RC registrada en el sistema.

pregunta_es_correcta(P, R) :- respuesta_correcta(P, RC), R = RC


## Hechos
- tema(T): T es un tema del sistema
- subtema(T, S): S es un subtema del tema T
- pregunta(S, P): P es una pregunta del subtema S
respuesta_correcta(P, R): R es la respuesta correcta de la pregunta P

## Reglas
- pregunta_es_del_tema(P, T): La pregunta P pertenece al tema T
- pregunta_es_correcta(P, R): La respuesta R es correcta para la pregunta P