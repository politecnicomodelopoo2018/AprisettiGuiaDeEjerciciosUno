class alumno(object):

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
        self.listaDeNotas.append(notaAIngresar)