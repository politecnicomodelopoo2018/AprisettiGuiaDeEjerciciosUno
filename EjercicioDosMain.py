import datetime

from random import randint
from EjercicioUno import Alumno
from EjercicioDos import Materias

pepito = Alumno()

matematica = Materias()
matematica.setNombreMateria("Matematica")
miniK = Materias()
miniK.setNombreMateria("MiniK")
pruscino = Materias()
pruscino.setNombreMateria("Pruscino")

'''pepito.listaDeMaterias = [matematica, miniK, pruscino]'''

pepito.setMateria(matematica)
pepito.setMateria(miniK)
pepito.setMateria(pruscino)

print("Escriba CHAU para dejar de ingresar notas")

for i in pepito.listaDeMaterias:

    i.listaDeNotas = [(randint(1, 10)),(randint(1, 10)),(randint(1, 10))]
    '''i.listaDeNotas = [int(input()), int(input()), int(input())]'''
    ''' nota = 0
     while(nota != "CHAU"):
         nota = input()
         if(nota == "CHAU"):
            break
         nota = int(nota)
         i.listaDeNotas = [nota] '''


for item in pepito.listaDeMaterias:
    print (item.getNombre())
    print (item.getPromedio())
