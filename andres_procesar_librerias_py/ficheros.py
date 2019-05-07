
#   Andrés Fernández Burón
#
#   andres_develops@outlook.es
#   Mayo 2019


#   Importo ficheros Python del mismo directorio que este script
import texto
import consola


#   Importo librerías :
import os



#
#   VARIABLES GLOBALES :
#




sist_cod_texto = "ISO-8859-1"



# Inicialización de variables del fichero/módulo
#este_separador = "/"
if os.name == "posix" :
    este_separador = "/"
else :
    este_separador = "\\"



#
#   MÉTODOS :
#
#   get_separador_path( path_completo )
#
#   get_dir_usuario()
#
#   es_directorio( path_completo )
#   es_fichero( path_completo )
#
#
#   get_nombre_fichero( path_completo )
#
#   es_ubicacion_actual( path_completo )
#
#   crear_directorio( path )
#   crear_directorio_recursivamente( path )
#
#   get_lineas_fichero( path_fichero )
#   escribir_fichero( path_fichero, lineas )
#





# Setter para el separador de paths, en base al SO
def get_separador_path() :
    return este_separador




# Devuelvo el path del directorio del usuario
def get_dir_usuario() :
    from os.path import expanduser
    #print( expanduser( "~" ) )
    return expanduser( "~" )










# Compruebo si es un Fichero o si es un Directorio
#partes_path = path_completo.split( '.' )
def es_directorio( path_completo ) :
    separador_path = get_separador_path( path_completo )
    if path_completo.find('.') != -1 and path_completo.find('.') > path_completo.find(separador_path) :
        #print( 'Es un fichero', end='' )
        return False
    else :
        #print( 'Es un directorio', end='' )
        if os.path.isdir( path ) :
            return True
        #print( 'Es un fichero sin extensión' )
        return False




# Compruebo si es un Fichero o si es un Directorio
#partes_path = path_completo.split( '.' )
def es_fichero( path_completo ) :
    separador_path = get_separador_path()
    if path_completo.find('.') != -1 and path_completo.find('.') > path_completo.find(separador_path) :
        #print( 'Es un fichero', end='' )
        return True
    else :
        #print( 'Es un directorio', end='' ) #o un fichero sin extensión' )
        return False






"""
# Obtengo el carácter que separa las partes del path
def get_separador_path( path_completo ) :
    if path_completo != "" :
        partes_path = path_completo.split( '/' )
        if len(partes_path) > 0 :
            separador_path = '/'
        else :
            partes_path = path_completo.split( '\\' )
            if len(partes_path) > 0 :
                separador_path = '\\'
            else :
                separador_path = '/'
        #print( "El separador de path es %s" % separador_path )
        return separador_path
    else :
        return ""
"""








# Obtengo el nombre de un fichero
# Si es un directorio o No tiene extensión, de vuelvo ""
def get_nombre_fichero( path_completo ) :
    if path_completo != "" :
        separador_path = get_separador_path()
        if( es_fichero( path_completo ) ) :
            partes_nombre_fichero = path_completo.partition( separador_path )
            return partes_nombre_fichero[ len(partes_nombre_fichero)-1 ]
    return ""







# Compruebo si está en una ruta o no (directorio actual)
def es_ubicacion_actual( path_completo ) :
    if path_completo.count( separador_path ) == 0 :
        print( ' dentro el directorio actual' )
    else :
        print( ' en una ruta compuesta por %s directorios' % path_completo.count(separador_path) )



#



# Si es un Fichero, lo copio a su destino

# path + fichero

# fichero en dir actual (solo nombre.ext)



# Si es un Directorio, lo recorro recursivamente,
# almacenando la estructura de ficheros en memoria,
# para copiar el contenido a su destino

# path con varios directorios

# un solo directorio




# Creo un directorio, si no existe
def crear_directorio( path ) :
    if not os.path.exists( path ) :
        os.makedirs( path )



# Creo directorios, recursivamente y si no existen
def crear_directorio_recursivamente( path_completo ) :
    if not os.path.exists( path_completo ) :
        os.makedirs( path_completo )






# Devuelvo una Lista con las líneas leídas del fichero de entrada
def get_lineas_fichero( path_fichero ) :
    print( "_______________________________________________________________" )
    print( "Lectura  " )#, end='' )
    print( f"Fichero  : {get_nombre_fichero( path_fichero )}" )
    print( f"Path  : {path_fichero}" )
    print( "_______________________________________________________________" )
    lineas = []
    with open( path_fichero, 'r', encoding=sist_cod_texto ) as fichero_entrada :
        for linea in fichero_entrada :
            #linea = texto.normalizar_texto( linea.lstrip().rstrip()  )
            linea = linea.lstrip().rstrip()
            lineas.append( linea )
            print( linea )
        fichero_entrada.close()
    print( )
    print( "_______________________________________________________________" )
    print( "Fichero leído !" )
    consola.esperar_usuario( "" )#consola.esperar_y_limpiar()
    return lineas






# Escribo una Lista de líneas en un fichero de salida
def escribir_fichero( path_fichero, lineas ) :
     #print( "===============================================================" )
    #print( "_______________________________________________________________" )
    print( "---------------------------------------------------------------" )
    print( "Escritura  " )#, end='' )
    print( f"Fichero  : {get_nombre_fichero( path_fichero )}" )
    print( f"Path  : {path_fichero}" )
    #print( "---------------------------------------------------------------" )
    print( "..............................................................." )
    with open( path_fichero, 'w', encoding=sist_cod_texto ) as fichero_salida :
        for linea in lineas :
            fichero_salida.write( "%s\n" % linea )
            print( linea )
    fichero_salida.close()
    print( )
    print( "_______________________________________________________________" )
    #print( "..............................................................." )
    print( "Fichero escrito !" )
    consola.esperar_usuario( "" )#consola.esperar_y_limpiar()
