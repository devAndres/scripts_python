

#   Andrés Fernández Burón
#
#   andres_develops@outlook.es
#   Mayo 2019


#   Importo ficheros Python del mismo directorio que este script
import texto


#   Importo librerías
from time import sleep
import os
from platform import python_version
from datetime import datetime, date#, time, timedelta




#
#   ATRIBUTOS GLOBALES :
#


ANCHO_CONSOLA = 100

este_so = ""
com_limpiar_pantalla = ""



if este_so == "posix" :
    com_limpiar_pantalla = "clear"
elif este_so == "ce" or este_so == "" or este_so == "nt" :
    com_limpiar_pantalla = "cls"
else :
    com_limpiar_pantalla = "clear"
    print( "Este SO no es Windows ni Unix !" )






#
#   MÉTODOS :
#
#   iniciar_script()
#   finalizar_script()
#
#   print_info()
#

#
#   print_cabecera( titulo, char )
#   print_menu( elementos )
#   print_mensaje( mensaje )
#
#   limpiar_consola()
#   esperar_usuario( "" )
#   esperar_y_limpiar()
#



# Inicio el Script y su GUI en Consola
def iniciar_script( titulo ) :
    limpiar_consola()
    print_cabecera( titulo, "=" )
    sleep( 0.5 )
    print_info()
    sleep( 0.5 )



# Finalizo el Script
def finalizar_script() :
    sleep( 0.5 )
    print()
    for i in range(0, ANCHO_CONSOLA) :
        print( "_", end="" )
        #time.sleep( 0.05 )
    print()
    print( "Fin de programa" )
    esperar_y_limpiar()
    from sys import exit
    exit()





# Imprimo info (v de Python, SO, Fechay Hora)
def print_info() :
    este_so = os.name
    print()
    print( "Este Sistema Operativo es %s." % este_so.capitalize() )
    print( "La versión de Python %s" % python_version() )
    fechaHora = datetime.strftime( datetime.today(), "%d-%m-%y %I:%m %p" )
    print( "%s\n" % fechaHora )
    sleep( 0.05 )
    print()




# Imprimo una cabecera
def print_cabecera( titulo, char ) :
    global ANCHO_CONSOLA
    if len(titulo) % 2 != 0 :
        ANCHO_CONSOLA += 1
    for i in range(0, ANCHO_CONSOLA) :
        print( "%s" % char, end="" )
        #sleep( 0.05 )
    print()
    ancho_aux = ANCHO_CONSOLA
    ancho_aux -= len(titulo) + 2
    ancho_aux //= 2
    for i in range( 0, ancho_aux ) :
        print( "%s" % char, end="" )
        #sleep( 0.05 )
    print( " %s " % titulo, end="" )
    for i in range( 0, ancho_aux ) :
        print( "%s" % char, end="" )
        #sleep( 0.05 )
    print()
    for i in range( 0, ANCHO_CONSOLA ) :
        print( "%s" % char, end="" )
        #sleep( 0.05 )
    print()




# Imprimo un menú y devuelvo la opción (numérica introducida por el usuario)
def print_menu( elementos ) :
    num_elementos = len( elementos )
    while True :
        print_cabecera( elementos[0], "=" )
        print()
        op = int( -1 )
        for i in range( 1, num_elementos ) :
            print( f"  {i}\t{elementos[i]}" )
        else :
            print()
            print( " -1\tPara salir" )
            print()
            print( f"Introduce un valor :  ", end="" )
        try :
            op = int( input() )
            if op in range( 0, num_elementos ) or op == -1 :
                return op
            else :
                print_mensaje( f"Opción no válida !\n\n\tIntroduce un valor de 1 a {num_elementos-1}" )
        except ValueError :
            print_mensaje( "Valor incorrecto introducido !\n\n\tTienes que introducir un número !" )
    limpiar_consola()





# Limpio la consola
def limpiar_consola() :
    sleep( 0.75 )
    #os.system( com_limpiar_pantalla )
    os.system( "clear" )





# Muestro un mensaje +-
def print_mensaje( mensaje ) :
    limpiar_consola()
    print( f"\n\n\n\n\n\n\t{ mensaje }" )
    limpiar_consola()


# Espero a que el usuario pulse ENTER
def esperar_usuario( mensaje ) :
    print()
    if mensaje == "" :
        mensaje = "Pulsa ENTER para continuar .... "
    input( mensaje )
    print()



# Espero a que el usuario pulse ENTER
def esperar_y_limpiar() :#( mensaje ) :
    esperar_usuario( "" )
    limpiar_consola()
