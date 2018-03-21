import datetime

class Empleado(object):

    def __init__(self, nombre = None, apellido = None, telefono = None, fechaDeNacimiento = None):
        self.nombre = nombre
        self.apellido = apellido
        self.telefono = telefono
        self.fechaDeNacimiento = fechaDeNacimiento
        self.listaDeDiasHabiles = [True, True, True, True, False, False, False]
        self.listaDeAsistencia = []

    def setNombre(self, nombreAIngresar):
        self.nombre=nombreAIngresar.title()

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

    def getPorcetajeDeAsistencia(self, año, mes):
        contador = 0
        contadorDias = 0
        for item in self.listaDeAsistencia:
            if(self.listaDeDiasHabiles[item.weekday()] == True):
                contador += 1
            else:
                continue
        for i in range(1, 31):
            fecha = datetime.date(año, mes, i).weekday()
            if(self.listaDeDiasHabiles[fecha] == True):
                contadorDias += 1
        print (contador)
        print (contadorDias)
        return contador/contadorDias


