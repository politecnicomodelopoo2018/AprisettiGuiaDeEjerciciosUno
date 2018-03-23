import datetime
from random import randint

class Jugador(Object):

    def __init__(self, nombreJugador = None, fechaDeNacimientoJugador = None, numeroJugador = None):

        self.nombreJugador = nombreJugador
        self.fechaDeNacimientoJugador = fechaDeNacimientoJugador
        self.numeroJugador = numeroJugador


    def setNombre(self, nombreAIngresar):

        self.nombreJugador = nombreAIngresar

    def setFechaDeNacimiento(self, fechaAIngresar):

        self.fechaDeNacimientoJugador = fechaAIngresar

    def setNumeroJugador(self, numeroAIngresar):

        self.numeroJugador = numeroAIngresar

    def camisetaJugador(self):

        self.numeroJugador = randint(1, 100)

