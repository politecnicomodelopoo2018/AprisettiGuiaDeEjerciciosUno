class alumno(object):

    nombre = ""
    apellido = ""
    fechaDeNacimiento = ""
    listaDeNotas = []

    def setNombre(self):
        self.nombre = input()
        return self.nombre
    def setApellido(self):
        self.apellido = input()
        return self.apellido
    def setFechaDeNacimiento(self):
        self.fechaDeNacimiento = input()
        return self.fechaDeNacimiento
    def setNota(self):
        nota = input()
        self.listaDeNotas.list.append(nota)
        return self.listaDeNotas