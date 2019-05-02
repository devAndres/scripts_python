#!/usr/bin/python
# -*- coding:utf-8 -*-

"""

Proceso Directorios

"""

# Importo librerías
import ficheros
import consola

import os

#import tkinter
#import calendar
#from TKinter import *
#from tkMessageBox import *




#
#   VARIABLES DE PROGRAMA :
#

opciones_menu = [
    "Menú principal",
    "Copiar",
    "Mover",
    "Otro",
    "Salir"
]


path_entrada = os.getcwd() + "dir_a/texto.txt"
path_salida = os.getcwd() + "dir_b"

partes_path = []
separador_path = '/'




#
#   PROGRAMA :
#



# Muestro la cabecera
consola.print_cabecera( "Programa Python 3", "=", 60 )
consola.print_info()


# Muestro menú
while true :
    op = consola.print_menu( opciones_menu )

    # Actúo en base a la acción introducida por el usuario
    if op == -1 :
        break
    else :
        print( "Has seleccionado : %s" % opciones_menu[op] )
    """
    if op == 1 :
        print()
    elif op == 2 :
        print()
    elif op == 3 :
        print()
    if op != -1 :
    """





















tkinter.Tcl().eval( "info patchlevel" )





#function getseparador(  )


#showerror( "Título", "Esto es el contenido" )
#askyes( "Título", "Esto es el contenido" )
#showerror( "Título", "Esto es el contenido" )

time.sleep( 0.5 )
print( "" )
print( "Fin de programa" )
print( "Pulsa ENTER para finalizar .", end="" )
for i in range( 0, 10 ) :
    print( ".", end="" )
    time.sleep( 0.45 )
input()
time.sleep( 0.5 )
limpiar_consola()
time.sleep( 0.5 )

