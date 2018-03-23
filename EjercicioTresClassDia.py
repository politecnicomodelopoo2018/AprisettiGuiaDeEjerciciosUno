import datetime

class Dia(Object):

    def __init__(self, nombreDia = None):

        self.nombreDia = nombreDia

        self.listaHorario = []

    def setNombre(self, nombreAIngresar):

        self.nombreDia = nombreAIngresar

    def setDisponibilidadHoraria(self, horaDisponible):

        self.listaHorario.append(horaDisponible)