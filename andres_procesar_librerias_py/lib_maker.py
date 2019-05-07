

#   Andrés Fernández Burón
#
#   andres_develops@outlook.es
#   Mayo 2019


#   Importo ficheros Python del mismo directorio que este script
import ficheros
import consola


# Importo librerías :
from time import sleep


#
#   ATRIBUTOS GLOBALES :
#

path_proyectos = ""
path_librerias = ""

nombre_proyecto = ""
nombre_libreria = ""






lineas_documentacion = []
lineas_header = []
lineas_source = []
lineas_ejemplo = []
lineas_desechadas = []



#
#   MÉTODOS :
#
#   get_num_version( path, pos )
#   actualizar_nombre_version( nombre_proyecto, pos )

#
#   redireccionar_linea( linea )
#
#   preparar_proyecto_entrada( _path_proyectos, _nombre_proyecto, subir_version )
#   preparar_libreria_salida( _path_librerias )
#
#   crear_libreria( path_proyectos, nombre_proyecto, subir_version )
#



# Devuelvo el nº de versión del proyecto (patrón: _v )
def get_num_version( pos ) :
    # CONTROLAR EXCEPCIÓN AL PARSEAR !!!!!!!!!!!! Ejemplo en consola.py/print_menu( opciones )  !!!!!!!!
    #print( nombre_proyecto[pos+2:] )
    num_version = int( nombre_proyecto[pos+2:] ) #+ 1
    # CONTROLAR EXCEPCIÓN AL PARSEAR !!!!!!!!!!!! Ejemplo en consola.py/print_menu( opciones )  !!!!!!!!
    return num_version







# Defino el nombre de la librería/proyecto con el nº de versión incrementado (patrón: _v )
def actualizar_nombre_version( pos ) :
    num_version = get_num_version( pos ) + 1
    global nombre_libreria
    nombre_libreria = nombre_proyecto[:len(nombre_proyecto)-1] + str( num_version )
    print( f"{nombre_proyecto} actualizado a versión nº {num_version} !" )







# Redirecciono
def redireccionar_lineas( lineas ) :
    global lineas_header, lineas_source, lineas_ejemplo
    for linea in lineas :
        lineas_documentacion.append( linea )
        lineas_header.append( linea )
        lineas_source.append( linea )
        lineas_ejemplo.append( linea )
        lineas_desechadas.append( linea )







#   ENTRADA DEL PROGRAMA :
#
#   En base al proyecto de entrada, defino el nombre de la librería y de sus componentes
#   Leo el fichero que contiene el proyecto y almaceno sus líneas en memoria
def preparar_proyecto_entrada( _path_proyectos, _nombre_proyecto, subir_version ) :

    global path_proyectos
    global nombre_proyecto
    global nombre_libreria

    path_proyectos = _path_proyectos

    nombre_proyecto = _nombre_proyecto

    print( "ENTRADA =============================================" )

    # Actualizo y Concreto el nombre de la librería de Salida (version++ si subir-version==True)

    nombre_libreria = nombre_proyecto
    if subir_version :
        pos = nombre_proyecto.find( "_v" )
        if( pos == -1 ) :
            #nombre_libreria = nombre_proyecto + "_v0"
            nombre_libreria += "_v0"
            print( f"---------{nombre_libreria}------------" )
        else :
            actualizar_nombre_version( pos )
            #print( f"Nombre Librería Salida     : {nombre_libreria}" )

   # Leo el fichero de entrada
    path_proyecto_entrada = path_proyectos + ficheros.get_separador_path() + nombre_proyecto + ficheros.get_separador_path() + nombre_proyecto + ".txt"
    lineas = ficheros.get_lineas_fichero( path_proyecto_entrada )
    redireccionar_lineas( lineas )




#   SALIDA DEL PROGRAMA :
#
#   Creo el directorio de la librería de salida
#   Escribo los ficheros 'header.h'
#   Escribo los ficheros source.cpp'
#   Creo el directorio de ejemplos
#   Escribo el fichero de ejemplo
def preparar_libreria_salida( _path_librerias ) :

    global path_librerias
    path_librerias = _path_librerias

    print( "== SALIDA  =============================================" )

    print( f"Path Librerias          : {path_librerias}" )

    # Defino el nombre de la librería
    global nombre_libreria
    nombre_libreria = "Andres_Lib_" + nombre_libreria
    print( f"Path Librerias          : {path_librerias}" )
    print( nombre_libreria )



    # Creo el directorio que va a contener la Librería
    # Si existe ya una librería (con ese mismo nº de version), ¿La borro? ó ¿La machaco?
    path_libreria = path_librerias + ficheros.get_separador_path() + nombre_libreria
    ficheros.crear_directorio_recursivamente( path_libreria )
    print( f"Path Libreria           : {path_libreria}" )
    print( f"Nombre Libreria         : {nombre_libreria}" )
    print( f"Nombre Proyecto         : {nombre_proyecto}" )




    # Defino los nombres de los ficheros
    # Fichero
    path_header = path_libreria + ficheros.get_separador_path() + nombre_libreria + ".h"
    ficheros.escribir_fichero( path_header, lineas_header )
    print( "Fichero Header" )



    # Fichero
    path_source = path_libreria + ficheros.get_separador_path() + nombre_libreria + ".cpp"
    print( "Fichero Source" )
    ficheros.escribir_fichero( path_source, lineas_source )



    # Creo el directorio de ejemplos
    path_dir_examples = path_libreria + ficheros.get_separador_path() + "examples"
    ficheros.crear_directorio( path_dir_examples )

    path_example = path_dir_examples + ficheros.get_separador_path() + nombre_proyecto + ".txt"
    print( "Fichero Ejemplo" )
    ficheros.escribir_fichero( path_example, lineas_ejemplo )

    # Escribo el fichero de salida
    #path = path_proyectos + ficheros.get_separador_path() + nombre_proyecto + ficheros.get_separador_path() + nombre_proyecto + ".txt"








    consola.print_mensaje( f"Librería {nombre_libreria} creada !" )


    lineas_documentacion.clear()
    lineas_header.clear()
    lineas_source.clear()
    lineas_ejemplo.clear()
    lineas_desechadas.clear()





    # Defino paths internos
    # Creo ficheros


"""
    path_entrada = os.getcwd() + "/" + nombre_proyecto + "/" + nombre_proyecto + ".txt"
    #path_proyectos_entrada + "/" + lista_dirs[op]

    path_salida = os.getcwd() + "/" + nombre_libreria + "/"


    nombre_fichero_entrada = ficheros.getNombreFichero( path_entrada )

    print( "ENTRADA :" )

    print( f"\tPath Completo :\n{ path_entrada }" )
    print( f"\tDirectorio :\n{ path_entrada }" )
    print( f"\tFichero :\n{ nombre_fichero_entrada }" )

    print( nombre_fichero_entrada )
    print()
    print( "SALIDA :" )
    print( subpath_salida_a )
    print( subpath_salida_b )
    print( subpath_salida_c )



    #sleep( 3 )
"""


def crearLibreria() :
    print( "Aquí crearía la librería" )





