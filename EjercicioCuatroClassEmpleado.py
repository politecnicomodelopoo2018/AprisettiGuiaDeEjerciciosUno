import datetime
from calendar import monthrange

class Empleado(object):

    def __init__(self, nombre = None, apellido = None, telefono = None, fechaDeNacimiento = None):
        self.nombre = nombre
        self.apellido = apellido
        self.telefono = telefono
        self.fechaDeNacimiento = fechaDeNacimiento
        self.listaDeDiasHabiles = [True, True, True, True, False, False, False]
        self.listaDeAsistencia = []

    def setNombre(self, nombreAIngresar):
        self.nombre = nombreAIngresar.title()

    def setApellido(self, apellidoIngresado):
        self.apellido = apellidoIngresado.title()

    def setFechaDeNacimiento(self, fechaDeNacimientoIngresada):
        self.fechaDeNacimiento = fechaDeNacimientoIngresada

    def setTelefono(self, telefonoIngresada):
        self.Telefono = telefonoIngresada

    def setDiasqueFue(self, diaQueFue):
        self.listaDeAsistencia.append(diaQueFue)

    def getDiasQueFue(self):
        return self.listaDeAsistencia

    def getPorcetajeDeAsistenciaMes(self, año, mes):
        contador = 0
        contadorDias = 0
        for item in self.listaDeAsistencia:
            if(mes == item.month):
                if(self.listaDeDiasHabiles[item.weekday()] == True):
                   contador += 1

                for i in range(1, monthrange(año, mes)+1):
                    fecha = datetime.date(año, mes, i).weekday()
                if(self.listaDeDiasHabiles[fecha] == True):
                    contadorDias += 1

                return contador/contadorDias
            else:
                return False