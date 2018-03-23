import datetime

class Equipo:
    def __init__(self, nombreEquipo = None, barrioEquipo = None):

        self.nombreEquipo = nombreEquipo
        self.barrioEquipo = barrioEquipo

        self.listaDisponibilidad = []
        self.listaJugadores = []
