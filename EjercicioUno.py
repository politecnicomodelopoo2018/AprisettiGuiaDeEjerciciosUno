import datetime
from datetime import timedelta

class Alumno(object):



    def __init__(self, nombre = None, apellido = None, fechaDeNacimiento = None):
        self.listaDeNotas = []
        self.nombre = nombre
        self.apellido = apellido
        self.fechaDeNacimiento = fechaDeNacimiento



    def setNombre(self, nombreIngresado):
        self.nombre = nombreIngresado.title()

    def setApellido(self, apellidoIngresado):
        self.apellido = apellidoIngresado.title()

    def setFechaDeNacimiento(self, fechaDeNacimientoIngresada):
        self.fechaDeNacimiento = fechaDeNacimientoIngresada

    def setNota(self, notaAIngresar):
        if(notaAIngresar > 10):
            return False
        if(notaAIngresar < 1):
            return False
        self.listaDeNotas.append(notaAIngresar)
        return True

    def getMayorNota(self):
        return max(self.listaDeNotas)

    def getMenorNota(self):
        return min(self.listaDeNotas)

    def getPromedioNota(self):
        return sum(self.listaDeNotas)/len(self.listaDeNotas)

    def getEdadActual(self):
        return (datetime.date.today() - self.fechaDeNacimiento)/365.25