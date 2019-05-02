

import time
import os
from platform import python_version
from datetime import datetime, date#, time, timedelta



# ATRIBUTOS :

este_so = ""
com_limpiar_pantalla = ""



#
#   MÉTODOS :
#
#   print_info()
#   print_cabecera( titulo, char )
#   print_menu( elementos )
#   limpiar_consola()
#


# Imprimo info (v de Python, SO, Fechay Hora)
def print_info() :
    este_so = os.name
    print( "Este Sistema Operativo es %s." % este_so )
    print( "La versión de Python %s" % python_version() )
    fechaHora = datetime.strftime( datetime.today(), "%d-%m-%y %I:%m %p" )
    print( "%s\n" % fechaHora )
    time.sleep( 0.05 )

# Imprimo una cabecera
def print_cabecera( titulo, char, ancho ) :
    if len(titulo) % 2 != 0 :
        ancho += 1
    for i in range(0, ancho) :
        print( "%s" % char, end="" )
        time.sleep( 0.05 )
    print()
    ancho -= len(titulo) + 2
    ancho //= 2
    for i in range( 0, ancho ) :
        print( "%s" % char, end="" )
        time.sleep( 0.05 )
    print( "%s" % titulo, end="" )
    for i in range( 0, ancho ) :
        print( "%s" % char, end="" )
        time.sleep( 0.05 )
    print()
    ancho += len(titulo) + 2
    ancho *= 2
    for i in range( 0, ancho ) :
        print( "%s" % char, end="" )
        time.sleep( 0.05 )



# Imprimo un menú y devuelvo la opción (numérica introducida por el usuario)
def print_menu( elementos ) :
    while True :
        print_cabecera( elementos[0], "=", 60 )
        op = int(-1)
        for i in range(1, len(elementos)-1) :
            print( f"\t {i}\t{elementos[i]}" )
        else :
            print( f"\t-1\t{elementos[len(elementos)-1]}", "\n" )
            print()
        try :
            op = int( input() )
            if op > 0 and op < len(opciones)-1 :
                return op
        except ValueError :
            limpiar_consola()
            print( "\n\n\n\n\n\n\tValor incorrecto introducido !" )
            time.sleep( 0.5 )
            limpiar_consola()





# Limpio la consola
def limpiar_consola() :
    if este_so == "posix" :
        com_limpiar_pantalla = "clear"
    elif este_so == "ce" or este_so == "" or este_so == "nt" :
        com_limpiar_pantalla = "cls"
    else :
        print( "Este SO no es Windows ni Unix !" )
    #os.system( com_limpiar_pantalla )
    os.system( "clear" )
    #print( "Ejecuto el comando %s" % com_limpiar_pantalla )

