
class Partido(Object)

    def __init__(self,numeroPartido = None ,numeroDia = None , Horario= None , equipo1 = None , equipo2 = None):

        self.numeroPartido = numeroPartido
        self.numeroDia = numeroDia
        self.Horario = Horario
        self.equipo1 = equipo1
        self.equipo2 = equipo2

    def setnumeroPartido(self , numeroPartidoAIgresar):

        self.numeroPartido = numeroPartidoAIgresar

    def setnumeroDia(self , numeroDiaAIngresar):

        self.numeroDia = numeroDiaAIngresar

    def setHorario(self , HorarioAIngresar):

        self.Horario= HorarioAIngresar

    def setEquipo1(self , equipo1AIngresar):

        self.equipo1 = equipo1AIngresar

    def setEquipo2(self , equipo2AIngresar):

        self.equipo2 = equipo2AIngresar

    def setDiferencia(self , Partido):

        for