#!/usr/bin/python
# -*- coding:utf-8 -*-



"""
====================================================================================================================
    Andrés Fernández Burón

    andres_develops@outlook.es
    Mayo 2019

    Programa :      Proceso Librerías
    Descripción :   Programa para crear librerías a partir de un proyecto
    Lenguaje :      Python 3
    Tipo :          Script con GUI en Consola
____________________________________________________________________________________________________________________
"""


# Importo fihceros Python del mismo directorio que este script
import consola
import ficheros
import lib_maker

# Importo librerías de Python 3
import os
from sys import exit

#import tkinter
#import calendar
#from TKinter import *
#from tkMessageBox import *




#
#   VARIABLES DE PROGRAMA :
#








path_proyectos_entrada = ficheros.get_dir_usuario() + "/code/scripts_python/DIR_PROYECTOS"
path_librerias_salida = ficheros.get_dir_usuario() + "/code/scripts_python/DIR_LIBRERIAS"






#
#   PROGRAMA :
#




# Muestro la cabecera
consola.iniciar_script( "Programa Python 3" )


# Muestro Menú y Actúo en base a la acción introducida por el usuario
opciones_menu = [
    "Menú principal",
    "Crear un proyecto",
    "Crear una librería a partir de un proyecto",
    "Actualizar una librería  a partir de un proyecto",
    "Crear librerías a partir de los proyectos",
    "Actualizar todas las librería",
    "Comprimir todas las librerías en ZIP",
    "Extraer ZIPs con librerías en directorio",
    "Opciones",
    "Cambiar rutas de E/S"
]
continuar = True
while continuar :
    op = consola.print_menu( opciones_menu )
    # OP-1  Salir
    if op == -1 :
        continuar = False

    # OP-1  Crear Librería
    if op == 1 :

        # PIDO ENTRADA POR TECLADO - PATHs E/S
        lista_dirs = os.listdir( path_proyectos_entrada )
        lista_dirs.insert( 0, "Proyectos" )
        op = consola.print_menu( lista_dirs )
        #print()

        if op != -1 :
            consola.print_mensaje( "Has seleccionado : %s" % lista_dirs[op] )
            lib_maker.preparar_proyecto_entrada(  path_proyectos_entrada, lista_dirs[op], True  )
            lib_maker.preparar_libreria_salida( path_librerias_salida )
            lib_maker.crearLibreria()


    """
    # OP-1  Actualizar todas las Librerías contenidas en el directorio
    elif op == 2 :
        print()
    elif op == 3 :
        print()
    if op != -1 :
    """




consola.finalizar_script()





















#tkinter.Tcl().eval( "info patchlevel" )





#function getseparador(  )


#showerror( "Título", "Esto es el contenido" )
#askyes( "Título", "Esto es el contenido" )
#showerror( "Título", "Esto es el contenido" )






