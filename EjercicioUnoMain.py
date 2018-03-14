from EjercicioUno import Alumno
import datetime

Aprile = Alumno()

Aprile.setNombre("Aprile")

Aprile.setApellido("Aprile")

Aprile.setFechaDeNacimiento(datetime.date(2001, 3, 8))

Aprile.setNota(1)

Aprile.setNota(3)

print (Aprile.getEdadActual())
print (Aprile.getPromedioNota())
print (Aprile.getMenorNota())
print (Aprile.getMayorNota())
