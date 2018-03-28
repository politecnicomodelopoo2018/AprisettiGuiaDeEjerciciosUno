import datetime
from random import randint
from EjercicioTresClassJugador import Jugador

class Equipo(Object):

    def __init__(self, nombreEquipo = None, barrioEquipo = None):

        self.nombreEquipo = nombreEquipo
        self.barrioEquipo = barrioEquipo

        self.listaDisponibilidadDia = [[False , False , False][False , False , False][False , False , False][False , False , False][False , False , False][False , False , False]]
        self.listaJugadores = []


    def setNombreEquipo(self, nombreAIngresar):

        self.nombreEquipo = nombreAIngresar

    def setBarrioEquipo(self, barrioAIngresar):

        self.barrioEquipo = barrioAIngresar

    def setDisponibilidadDias(self, dias):

        self.listaDisponibilidadDia.append(dias)


    def organizarNumeros(self):

        for item in self.listaJugadores:
            for jugador in self.listaJugadores:
                if(item.numeroJugador == jugador.numeroJugador):
                    item.camisetaJugador()

    def coordinacion(self, dia, hora):
         return self.listaDisponibilidadDia[[dia][hora]]

