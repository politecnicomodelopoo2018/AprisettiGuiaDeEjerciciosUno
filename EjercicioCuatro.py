import datetime

class Empleado(object):

    def __init__(self, nombre = None, apellido = None, telefono = None, fechaDeNacimiento = None):
        self.nombre = nombre
        self.apellido = apellido
        self.telefono = telefono
        self.fechaDeNacimiento = fechaDeNacimiento
        self.listaDeDiasHabiles = [True, True, True, False, False]
        self.listaDeAsistencia = []

    def setNombre(self, nombreAIngresar):
        self.nombre=nombreAIngresar.title()

    def setApellido(self, apellidoIngresado):
        self.apellido = apellidoIngresado.title()

    def setFechaDeNacimiento(self, fechaDeNacimientoIngresada):
        self.fechaDeNacimiento = fechaDeNacimientoIngresada

    def setTelefono(self, Telefono):
        self.Telefono= Telefono

    def getDiasQueFue(self):
