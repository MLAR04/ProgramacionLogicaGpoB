# Practica SLD (#5)

Equipo #4 **Gastronomia**
22760905 - Joska Szoke Filatoff

## Base de Conocimiento

### [Leyes](sld_practice.py)

"Si una receta es vegetariana y no incluye lácteos, huevos o miel ENTONCES es vegana."

"SI una receta cumple con el 75% de VERDURAS, CARBOHIDRATOS Y PROTEINAS seleccionadas ENTONCES se muestra."

### [Hechos](hechos.py)

```prolog
receta(spaghetti_con_pure_de_berenjena, vegana, [
    ingrediente(tofu, proteina, '1/2 taza troceado'),
    ingrediente(spaghetti_integral, carbohidrato, '250 g'),
    ingrediente(berenjena, verdura, '1 unidad'),
    ingrediente(ajo, verdura, '2 dientes'),
    ingrediente(aceite_de_oliva, liquido, '2 cucharadas'),
    ingrediente(jugo_de_limon, liquido, '1 cucharada'),
    ingrediente(sal, condimento, 'al gusto'),
    ingrediente(perejil, hierba, 'al gusto')
])
```

```prolog
receta(tacos_de_champiñones, vegana, [
    ingrediente(tortillas_de_maiz, carbohidrato, '9 unidades'),
    ingrediente(aceite_vegetal, aceite, '2 cucharadas'),
    ingrediente(champiñones, verdura, '500g'),
    ingrediente(cebolla, verdura, '1 pieza'),
    ingrediente(chiles_serranos, verdura, '2 unidades'),
    ingrediente(limones, verdura, '3 unidades'),
    ingrediente(sal, condimento, 'al gusto'),
    ingrediente(pimienta, condimento, 'al gusto'),
    ingrediente(cilantro, hierba, '1/2 taza'),
    ingrediente(ajo, otros, '2 dientes')
])
```

```prolog
receta(quesadillas_flor_calabaza, vegetariana, [
    ingrediente(tortilla_de_maiz, carbohidrato, '8 unidades'),
    ingrediente(flor_calabaza, verdura, '1 taza'),
    ingrediente(queso_fresco, lacteo, '100 g'),
    ingrediente(aceite_vegetal, aceite, '1 cucharada'),
    ingrediente(sal, condimento, 'al gusto'),
    ingrediente(ajo, otros, '1 diente')
])
```

```prolog
receta(tacos_al_pastor, normal, [
    ingrediente(cerdo, proteina, '500 g'),
    ingrediente(tortilla_de_maiz, carbohidrato, '8 unidades'),
    ingrediente(cebolla, verdura, '1/2 unidad'),
    ingrediente(cilantro, verdura, 'al gusto'),
    ingrediente(piña, verdura, '1/2 taza picada'),
    ingrediente(sal, condimento, 'al gusto'),
    ingrediente(achiote, otros, '2 cucharadas'),
    ingrediente(chiles_secos, otros, '3 unidades'),
    ingrediente(ajo, otros, '2 dientes'),
    ingrediente(jugo_de_piña, liquido, '1/4 taza'),
    ingrediente(aceite_vegetal, aceite, '2 cucharadas')
])
```

```prolog
receta(pozole, normal, [
    ingrediente(carne_de_cerdo, proteina, '1kg (maciza y costilla)'),
    ingrediente(huevo, proteina, '1 unidad'),
    ingrediente(maiz_pozolero, carbohidrato, '500g'),
    ingrediente(tostadas, carbohidrato, '12 unidades'),
    ingrediente(cebolla, verdura, '1 pieza'),
    ingrediente(cebolla_picada, verdura, '1/2 taza'),
    ingrediente(lechuga, verdura, '1 taza (finamente picada)'),
    ingrediente(rábanos, verdura, '1/2 taza (en rodajas)'),
    ingrediente(limones, verdura, '4 unidades'),
    ingrediente(chiles_guajillo, verdura, '6 unidades'),
    ingrediente(ajos, verdura, '4 dientes'),
    ingrediente(agua, liquido, '3 litros'),
    ingrediente(sal, condimento, 'al gusto'),
    ingrediente(orégano_seco, condimento, '1 cucharada')
])
```