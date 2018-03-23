import datetime

from EjercicioCuatroClassEmpleado import Empleado
from EjercicioCuatroClassEmpresa import Empresa

pepe = Empleado()

pepe.setNombre("pepe")
pepe.setApellido("pepe2")
pepe.setFechaDeNacimiento(datetime.date(1982, 12, 26))

'''continuar = True

while(continuar):
    año = int(input())
    mes = int(input())
    dia = int(input())
    pepe.setDiasqueFue(datetime.date(año, mes, dia))
    seguir = input()

    if(seguir == "no"):
        continuar = False
    else:
        continue'''

for i in range(1, 30):
    pepe.setDiasqueFue(datetime.date(2000, 4, i))

print(pepe.getPorcetajeDeAsistenciaMes(2000, 4))