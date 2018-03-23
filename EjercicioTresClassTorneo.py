import datetime
from EjercicioTresClassEquipo import Equipo

class Torneo(Object):

    def __init__(self, nombreTorneo = None):

        self.nombreTorneo = nombreTorneo

        self.listaEquipos = []
        self.listaFixture = []

    def setListaEquipo(self, equipoAIngresar):

        self.listaEquipos.append(equipoAIngresar)

    def organizarFixture(self):

        for item in self.listaEquipos:
            for equipo in self.listaEquipos:
                for i in range(5):
                    for j in range(2):
                        if(item.coordinacion(i, j) == equipo.coordinacion(i, j):


