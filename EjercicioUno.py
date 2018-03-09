class alumno(object):

    nombre = ""
    apellido = ""
    fechaDeNacimiento = ""
    listaDeNotas = []

    def setNombre(self, nombreIngresado):
        self.nombre = nombreIngresado
    def setApellido(self, apellidoIngresado):
        self.apellido = apellidoIngresado
    def setFechaDeNacimiento(self, fechaDeNacimientoIngresada):
        self.fechaDeNacimiento = fechaDeNacimientoIngresada
    def setNota(self, notaAIngresar):
        self.listaDeNotas.append(nota)