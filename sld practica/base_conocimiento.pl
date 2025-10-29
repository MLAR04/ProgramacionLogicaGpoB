% ==== Hechos ====
hotel('Hotel_Sol', 'Cancún', 'lujo', 2000).
hotel('Hostal_Playa', 'Cancún', 'económico', 500).
hotel('Hotel_Lujo', 'Los_Cabos', 'lujo', 5000).
hotel('Cabaña_Bosque', 'Valle_de_Bravo', 'rural', 1200).
actividad('Snorkel', 'Cancún', 'acuática', 700).
actividad('Paracaidismo', 'Los_Cabos', 'extrema', 3000).
actividad('Museo_Frida_Kahlo', 'Ciudad_de_México', 'cultural', 200).
actividad('Kayak', 'Valle_de_Bravo', 'acuática', 600).
actividad('Senderismo', 'Valle_de_Bravo', 'aventura', 0).
actividad('Tour_Tequila', 'Guadalajara', 'gastronómica', 350).

% ==== Reglas (Cláusulas de Horn) ====
% 1. Un lugar es turístico si tiene al menos una actividad.
turistico(Lugar) :- actividad(_, Lugar, _, _).

% 2. Un hotel es accesible si su precio es menor o igual a un presupuesto dado.
accesible(Hotel, Lugar, Presupuesto) :- hotel(Hotel, Lugar, _, Precio), Precio =< Presupuesto.
