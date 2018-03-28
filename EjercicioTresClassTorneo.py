import datetime
from EjercicioTresClassEquipo import Equipo
from EjercicioTresClassPartido import Partido

class Torneo(Object):

    def __init__(self, nombreTorneo = None):

        self.nombreTorneo = nombreTorneo

        self.listaEquipos = []
        self.listaFixture = []

    def setDiferencia(self, Partido):

        for item in self.listaFixture:
            if Partido  == self.listaFixture[item]
                return False

    def setListaEquipo(self, equipoAIngresar):

        self.listaEquipos.append(equipoAIngresar)

    def setNombreTorneo(self, nombreIngresar):

        self.nombreTorneo = nombreIngresar


    def organizarFixture(self):

        for item in self.listaEquipos:
            numerito= 0
            for equipo in self.listaEquipos:
                for i in range(5):
                    for j in range(2):
                        if item.coordinacion(i, j) == equipo.coordinacion(i, j):

                            L = Partido()
                            L.numeroDia = i
                            L.Horario = j
                            L.equipo1 = item
                            L.equipo2 = equipo
                            L.numeroPartido = numerito

                                if self.setDiferencia(L)

                                   self.listaFixture.append(L)

                                      break


