from typing import List
from entities.clase_jugadores import Jugadores 

class Equipos():

    def __init__(self, nombre, lista_de_jugadores_equipo):
        self._nombre = nombre 
        self._lista_de_jugadores_equipo = lista_de_jugadores_equipo

    @property
    def nombre (self):
        return self._nombre
    
    @property
    def get_jugadores_equipo (self) -> List [Jugadores]: 
        return self._lista_de_jugadores_equipo 

    
