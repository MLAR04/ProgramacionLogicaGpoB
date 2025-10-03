x# Practica No.4

## Detector de Enfermedades


**Desarrollo de la práctica**

Con base a los datos que sen encuentren en la Base de  Conocimiento, Desarrolla el motor de inferencia en código en Python  que diagnostique la enfermedad con base en los síntomas.

**Base de Conocimiento**

Enfermedades{

Gripe (tos , dolor de cabeza)

Covid (fiebre, tos, cansancio, pérdida del olfato)

Migraña ( dolor de cabeza, náuseas)

Resfriado (congestión nasal, fiebre, tos)

}


**HECHOS**

-Tiene tos y dolor de cabeza, tiene Gripe

-Tiene fiebre, tos, cansancio y perdida de olfato, tiene Covid

-Tiene dolor de cabeza y náuseas, tiene Migraña

-Tiene congestión nasal, febre y tos, tiene Resfriado

-No tiene síntomas, no se puede diagnosticar

-Tiene síntomas de varias enfermedades, puede ser posible alguna 


**REGLAS**

a)Si tienes todos los síntomas de un enfermedad -> tienes una enfermedad

b)Si no se tiene todos los síntomas o no presenta nignuno -> no se puede diagnosticar 

c)Si se tienen sistomas de diferentes enfermedades -> es incierta o posible alguna enfermendad

