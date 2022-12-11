from MVT.models import Familiar

Familiar(nombre="Lucas", direccion="Uruguay 1200", numero_dni=40863460, nacimiento=str("1999-01-08")).save()
Familiar(nombre="Florencia", direccion="Uruguay 1200", numero_dni=37598874, nacimiento=str("1994-02-26")).save()
Familiar(nombre="Silvana", direccion="Uruguay 1200", numero_dni=23154839, nacimiento=str("1972-12-28")).save()

print("Los datos han sido cargado con éxito")