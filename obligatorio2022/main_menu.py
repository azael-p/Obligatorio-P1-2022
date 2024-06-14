from entities.clase_jugadores import Jugadores 
from entities.clase_equipos import Equipos
from entities.clase_datos import Datos
from entities.clase_consultas import Consultas 

class Menu():

    def inicio(): 

        lista_de_jugadores = []
        lista_de_equipos = [] 

        while True:

            print('Menu principal')
            print('Seleccione la opcion del menu:')
            print('1. Alta de jugador')
            print('2. Alta de equipo')
            print('3. Simular partido único')
            print('4. Realizar consultas')
            print('5. Finalizar programa')

            a = input('Ingrese Número:')

            if a.isdigit():
                a = int(a) 
            else:
                print('Uno o más datos ingresados son inválidos, intente nuevamente')
                continue

            if a == 1:

                print('Alta de jugador')

                try:

                    pasaporte = Datos.pedir_pasaporte(lista_de_jugadores) 
                    nombre = Datos.pedir_nombre() 
                    fecha_de_nacimiento = Datos.pedir_fecha()
                    pais_de_nacimiento = Datos.pedir_pais_de_nacimeinto()
                    posicion = Datos.pedir_posicion() 
                    puntaje = Datos.pedir_puntaje()
                    tiene_equipo = False

                    obj_jugador = Jugadores(pasaporte, nombre, fecha_de_nacimiento, pais_de_nacimiento, posicion, puntaje, tiene_equipo)

                    lista_de_jugadores.append(obj_jugador) 

                    
                    print('Jugador registrado con éxito') 

                except ValueError:
                    print('Uno o más datos ingresados son inválidos, intente nuevamente')
                    continue

            if a == 2:

                print('Alta de equipo equipo')

                try:

                    nombre_equipo = Datos.pedir_nombre_equipo(lista_de_equipos) 
                    lista_de_jugadores_equipo = Datos.aniadir_jugadores_equipo(lista_de_jugadores)
                    obj_equipo = Equipos(nombre_equipo, lista_de_jugadores_equipo) 

                    lista_de_equipos.append(obj_equipo)
                    
                    print('Equipo registrado con éxito')

                except ValueError:
                    print('Uno o más datos ingresados son inválidos, intente nuevamente')
                    continue

            if a == 3:

                try:
                    Datos.simular_partido(lista_de_equipos)

                except ValueError:
                    print('Uno o más datos ingresados son inválidos, intente nuevamente')
                    continue

            if a == 4: 
                try:
                    print('1. Determine los 5 jugadores con mejor puntaje de un equipo (basados en su puntaje)')
                    print('2. Determine los 10 mejores jugadores de todo el muendial (basados en su puntaje)')
                    print('3. Determine los 7 jugadores más viejos del mundial')
                    print('4. Determine el equipo con mejores defensas del mundial (basados en su puntaje promedio)')

                    a = input('Ingrese número: ')

                    if a.isdigit():
                        a = int(a) 

                        if a > 4 or a < 1:
                            raise ValueError

                        elif a == 1:
                                Consultas.consulta1(lista_de_equipos)

                        elif a == 2:
                                Consultas.consulta2(lista_de_jugadores)

                        elif a == 3:
                                Consultas.consulta3(lista_de_jugadores)

                        elif a == 4: 
                                Consultas.consulta4(lista_de_equipos)
                    else:
                        raise ValueError

                except ValueError:
                    print('Uno o más datos ingresados son inválidos, intente nuevamente')
                    continue

            if a == 5:
                print('Programa finalizado')
                break 
            
            if a < 1  or a > 5 :
                print('Uno o más datos ingresados son inválidos, intente nuevamente')
                continue


if __name__ == '__main__':

    Menu.inicio()  