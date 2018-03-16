import datetime
from EjercicioDos import Materias
from datetime import timedelta

class Alumno(object):



    def __init__(self, nombre = None, apellido = None, fechaDeNacimiento = None):
        self.listaDeMaterias = []
        self.nombre = nombre
        self.apellido = apellido
        self.fechaDeNacimiento = fechaDeNacimiento



    def setNombre(self, nombreIngresado):
        self.nombre = nombreIngresado.title()

    def setApellido(self, apellidoIngresado):
        self.apellido = apellidoIngresado.title()

    def setFechaDeNacimiento(self, fechaDeNacimientoIngresada):
        self.fechaDeNacimiento = fechaDeNacimientoIngresada

    def setMateria(self, materia):
        self.listaDeMaterias.append(materia)

    def setNotaMateria(self, nombreMateria, notaAIngresar):
        for item in self.listaDeMaterias:
            if item.nombre == nombreMateria:
                item.setNota(notaAIngresar)
                return True

    def getMayorNota(self, nombreMateria):
        return max(self.listaDeMaterias[materia].getlistaDeNotas)

    def getMenorNota(self, nombreMateria):
        return min(self.listaDeMaterias[materia].getlistaDeNotas)

    def getPromedioMateria(self, nombreMateria):
        for item in self.listaDeMaterias:
            if item.nombre == nombreMateria:
                return item.getPromedio()

    def getPromedioMenorMateria(self):
        menorPromedio = 0
        for item in self.listaDeMaterias:
            J = item.getPromedio
            if menorPromedio > J:
                menorPromedio = item.getPromedio
        return menorPromedio

    def getPromedioMayorMateria(self):
        mayorPromedio = 0
        for item in self.listaDeMaterias:
            J = item.getPromedio
            if mayorPromedio < J:
                mayorPromedio = item.getPromedio
        return mayorPromedio

    def getEdadActual(self):
        return (datetime.date.today() - self.fechaDeNacimiento)/365.25
