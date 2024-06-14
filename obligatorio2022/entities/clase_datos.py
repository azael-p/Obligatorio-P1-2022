import datetime
from typing import List
from entities.clase_equipos import Equipos
from entities.clase_jugadores import Jugadores

class Datos(): 

    def pedir_pasaporte(lista_de_jugadores: List [Jugadores]):
        pasaporte = (input('Ingrese pasaporte: '))
        if len(str(pasaporte)) == 8 and pasaporte.isdigit():
            pasaporte = int(pasaporte)
            if len(lista_de_jugadores) == 0:   
                for x in  range(len(lista_de_jugadores)):
                    if pasaporte == lista_de_jugadores[x].get_pasaporte: 
                        raise ValueError
                else: 
                    return pasaporte 
            else:
                return pasaporte
        else:
            raise ValueError 
        
    def pedir_nombre():
        nombre = input('Ingrese nombre: ') 
        if nombre.replace(' ','').isalpha():
            return nombre
        else:
            raise ValueError 
            
    def pedir_fecha():     
        fecha = (input('Ingrese fecha de nacimiento con el formato DD/MM/YYYY : '))
        fecha = (datetime.datetime.strptime(fecha, '%d/%m/%Y')).date()  
        return fecha 

    def pedir_pais_de_nacimeinto():
        pais_de_nacimiento = input('Ingresse país de nacimeinto: ')
        return pais_de_nacimiento

    def verificar_posicion(posicion):

        if posicion.replace(' ','').isalpha():

            if posicion == 'arquero':
                return 'arquero' 

            elif posicion == 'defensa':
                return 'defensa'

            elif posicion == 'mediocampista':
                return 'mediocampista'

            elif posicion == 'delantero':
                return 'delantero'  

            else: 
                raise ValueError  

        else:
            raise ValueError

    def pedir_posicion():
        print('1. Arquero')
        print('2. Defensa')
        print('3. MedioCampiasta')
        print('4. Delantero')
        posicion = input('Ingrese posicion: ')

        posicion2 = Datos.verificar_posicion(posicion)
        

        return posicion2 

    def pedir_puntaje():
        puntaje = input('Ingrese puntaje: ')
        if puntaje.isdigit():
            puntaje = int(puntaje)
            if  0 < puntaje < 100:
                return puntaje
            else:
                raise ValueError
        else: 
            raise ValueError
    
    def pedir_nombre_equipo(lista_de_equipos: List [Equipos]):
        nombre = input('Ingrese nombre: ')
        for i in range(len(lista_de_equipos)):
            if lista_de_equipos[i].nombre == nombre: 
                raise ValueError
        else: 
            return nombre 

    def aniadir_jugadores_equipo(lista_de_jugadores: List [Jugadores]): 

        lista_de_jugadores_equipo = []

        goleros = 1
        defensas = 4
        medio_campistas = 3
        delanteros = 3 
        
        for i in range(11):

            pasaporte = (input('Ingrese pasaporte: '))

            if len(str(pasaporte)) == 8 and pasaporte.isdigit():
                pasaporte = int(pasaporte)

                jugador = Datos.verificar_pasaporte(lista_de_jugadores, pasaporte) 

                if  jugador != None:
                    if Datos.verificar_posicion2(jugador.get_posicion, goleros, defensas, medio_campistas, delanteros): 

                        if not jugador.get_tiene_equipo: 

                            lista_de_jugadores_equipo.append(jugador)

                        else:
                            raise ValueError
                    else:                    
                        print(jugador._nombre)
                        raise ValueError 
                else: 
                    raise ValueError
            else: 
                raise ValueError 


        if len(lista_de_jugadores_equipo) ==  11:
            return lista_de_jugadores_equipo
        else:
            raise ValueError
            
    def verificar_pasaporte(lista_de_jugadores: List [Jugadores], pasaporte):

        for x in lista_de_jugadores: 

            if pasaporte == x.get_pasaporte: 

                return x
        
        return None 

    def verificar_posicion2(posicion_jugador, goleros, defensas, medio_campistas, delanteros):
        

        if str.lower(posicion_jugador) == 'arquero':
            if goleros > 0:
                goleros-=1
                return True
            else:
                return False
    

        elif str.lower(posicion_jugador) == 'defensa':
            if defensas > 0:
                defensas -= 1
                return True
            else: 
                return False


        elif str.lower(posicion_jugador) == 'mediocampista':
            if medio_campistas > 0:
                medio_campistas -=1
                return True
            else: 
                return False


        elif str.lower(posicion_jugador) == 'delantero':    
            if delanteros > 0:
                delanteros -= 1
                return True
            else:
                return False 
                
    def tiene_equipo(tiene_equipo):

        if not tiene_equipo:
            tiene_equipo = True
            return True

        else:
            return False

    def verifircar_nombres_equipo(lista_de_equipos):

        nombre = input('Ingrese nombre del equipo: ')
        if nombre.replace(' ','').isalpha():
            for i in lista_de_equipos:
                if nombre in i.nombre:
                    return i 
            else:
                raise ValueError 
        else:
           raise ValueError 

    def calcular_puntaje_promedio(lista_de_equipos: List [Equipos] ,equipo: Equipos):

        lista_de_puntajes_equipo = [] 
        punateje_goleros = 0 
        puntaje_defensas = 0
        punatje_mediocampistas = 0 
        puntaje_delanteros = 0

        if equipo in lista_de_equipos:
        
            try :
                for jugador in equipo.get_jugadores_equipo: 
                    
                    if jugador.get_posicion == 'arquero':
                        punateje_goleros += jugador.get_puntaje

                    if jugador.get_posicion == 'defensa':
                        puntaje_defensas += jugador.get_puntaje 

                    if jugador.get_posicion == 'mediocampista': 
                        punatje_mediocampistas += jugador.get_puntaje

                    if jugador.get_posicion == 'delantero':
                        puntaje_delanteros += jugador.get_puntaje

                lista_de_puntajes_equipo.append(punateje_goleros)
                puntaje_defensas = puntaje_defensas/4
                lista_de_puntajes_equipo.append(puntaje_defensas)
                punatje_mediocampistas = punatje_mediocampistas/3
                lista_de_puntajes_equipo.append(punatje_mediocampistas)
                puntaje_delanteros = puntaje_delanteros/3
                lista_de_puntajes_equipo.append(puntaje_delanteros)
            except TypeError:
                print(equipo.get_jugadores_equipo) 
        

            return lista_de_puntajes_equipo

        else:
            raise ValueError
 
    def verificar_promedios(lista1, lista2):
        puntos = [0, 0] 
        #arqueros
        if lista1[0] == lista2[0]:
            puntos[0] += 1
            puntos[1] += 1
        
        elif lista1[0] > lista2[0]:
            puntos[0] += 1
        
        elif lista1[0] < lista2[0]:
            puntos[1] += 1

        #defensas
        if lista1[1] == lista2[1]:
            puntos[0] += 1
            puntos[1] += 1
        
        elif lista1[1] > lista2[1]:
            puntos[0] += 1
        
        elif lista1[1] < lista2[1]:
            puntos[1] += 1

        #mediocampistas
        if lista1[2] == lista2[2]:
            puntos[0] += 1
            puntos[1] += 1
        
        elif lista1[2] > lista2[2]:
            puntos[0] += 1

        elif lista1[2] < lista2[2]:
            puntos[1] += 1

        #delanteros
        if lista1[3] == lista2[3]:
            puntos[0] += 1
            puntos[1] += 1
        
        elif lista1[3] > lista2[3]:
            puntos[0] += 1
        
        elif lista1[3] < lista2[3]:
            puntos[1] += 1
        
        return puntos
        
    def simular_partido(lista_de_equipos): 

        if len(lista_de_equipos) >= 2:

            equipo1 = Datos.verifircar_nombres_equipo(lista_de_equipos)
            equipo2 = Datos.verifircar_nombres_equipo(lista_de_equipos) 
            promedios_1 = Datos.calcular_puntaje_promedio(lista_de_equipos ,equipo1) 
            promedios_2 = Datos.calcular_puntaje_promedio(lista_de_equipos ,equipo2)

            puntos  = Datos.verificar_promedios(promedios_1, promedios_2)

            print(equipo1.nombre, ': ', puntos[0], ' - ', puntos[1], ' :', equipo2.nombre) 
        else:
            raise ValueError

    def calcular_promedio_defensa(equipo:Equipos): 
        
        promedio_defensas = 0
        
        for jugador in equipo.get_jugadores_equipo:

            if jugador.get_posicion == 'defensa':
                promedio_defensas += jugador.get_puntaje

        return promedio_defensas/4 
