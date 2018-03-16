class Materias(object):

    def __init__(self, materia = None, listaDeNotas = None):

        materia = None
        listaDeNotas = []



    def setNombreMateria(self, nombreDeMateriaAIngresar):
        self.materia = nombreDeMateriaAIngresar

    def setNota(self, notaAIngresar):
        if (notaAIngresar > 10):
            return False
        if (notaAIngresar < 1):
            return False
        self.listaDeNotas.append(notaAIngresar)
        return True

    def getPromedio(self):
        return (sum(self.listaDeNotas) / len(self.listaDeNotas))

    def getMenorNota(self):
        return min(self.listaDeNotas)
    def getMayorNota(self):
        return max(self.listaDeNotas)