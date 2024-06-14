class Jugadores:
    
    def __init__(self, pasaporte, nombre, fecha_de_nacimiento, pais, posicion, puntaje, tiene_equipo):
        self._pasaporte = pasaporte
        self._nombre = nombre
        self._fecha_de_naciminto = fecha_de_nacimiento
        self._pais = pais
        self._posicion = posicion
        self._puntaje =puntaje
        self._tiene_equipo = tiene_equipo

    @property
    def get_pasaporte (self): 
        return self._pasaporte
    
    @property
    def get_nombre (self):
        return self._nombre

    @property 
    def get_fecha_de_nacimiento(self):
        return self._fecha_de_naciminto

    @property
    def get_pais (self):
        return self._pais
    
    @property
    def get_posicion (self):
        return self._posicion
    
    @property
    def get_puntaje (self):
        return self._puntaje

    @property
    def get_tiene_equipo (self):
        return self._tiene_equipo

    @get_tiene_equipo.setter
    def tiene_equipo(self, tiene_equipo):
        self._tiene_equipo = tiene_equipo