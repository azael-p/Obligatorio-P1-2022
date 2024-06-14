from datetime import date
from typing import List
from entities.clase_datos import Datos
from entities.clase_equipos import Equipos
from entities.clase_jugadores import Jugadores


class Consultas(): 

    def consulta1(lista_de_equipos: List [Equipos]):
        
        lista_jugadores = []

        if len(lista_de_equipos) >= 0:

            equipo = Datos.verifircar_nombres_equipo(lista_de_equipos)
            
            for x in range(11):

                lista_jugadores.append(equipo.get_jugadores_equipo[x]) 

            lista_jugadores = sorted(lista_jugadores, key = lambda i:(-i.get_puntaje, i.get_nombre))

            for j in range(5):

                print('TOP',j+1,'. ',lista_jugadores[j].get_nombre, '-', lista_jugadores[j].get_puntaje)  
        else: 
            raise ValueError

    def consulta2(lista_de_jugadores: List [Jugadores]):

        if len(lista_de_jugadores) >= 7:
            lista_de_jugadores = sorted(lista_de_jugadores, key = lambda x:(-x.get_puntaje, x.get_nombre))

            for i in range(10):
                print('TOP', i+1, '. ', lista_de_jugadores[i].get_nombre, '-', lista_de_jugadores[i].get_puntaje)
        else:
            raise ValueError

    def consulta3(lista_de_jugadores: List [Jugadores]):

        if len(lista_de_jugadores) > 7:
        
            lista_de_jugadores = sorted(lista_de_jugadores, key = lambda x:(x.get_fecha_de_nacimiento.year, x.get_nombre))

            for i in range(7):
                
                now = date.today().year 

                edad =   now  - lista_de_jugadores[i].get_fecha_de_nacimiento.year

                print('TOP', i+1, '. ', lista_de_jugadores[i].get_nombre, '-', edad , 'Años') 

        else:
            raise ValueError

    def consulta4(lista_de_equipos: List [Equipos]):

        if len(lista_de_equipos) > 0: 
 
            equipo_tqmp = None
            max = 0
            for equipo in lista_de_equipos :
                promedio = Datos.calcular_promedio_defensa(equipo)

                if promedio >= max:
                    max = promedio
                    equipo_tqmp = equipo

            print(equipo_tqmp.nombre, ' - ', max) 

        else:
            raise ValueError 