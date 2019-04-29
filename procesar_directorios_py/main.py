"""

Proceso Directorios

"""

# Importo librerías
import time
import os


path_entrada = ""
path_salida = ""

partes_path
separador_path

# Obtengo el carácter que separa las partes del path
if path_entrada != ""
    partes_path = path_entrada.split( '/' )
    if partes_path.length() > 0
        separador_path = '/'
    partes_path = path_entrada.split( '\' )
    if partes_path.length() > 0
        separador_path = '\'
    else
        separador = '/'



# Compruebo si es un Fichero o si es un Directorio
#partes_path = path_entrada.split( '.' )
if path-entrada.find('.') != -1 and path_entrada.find('.') > path_entrada.find(separador_path)
    print( 'Es un fichero' )
else
    print( 'Es un directorio' ) #o un fichero sin extensión' )


# Compruebo si está en una ruta o no (directorio actual)
if path_entrada.find( separador_path ) == -1
    print( ' dentro el directorio actual' )
else
    print( ' en una ruta compuesta por %s directorios' % path_entrada.count(separador_path) )

#



# Si es un Fichero, lo copio a su destino

# path + fichero

# fichero en dir actual (solo nombre.ext)



# Si es un Directorio, lo recorro recursivamente,
# almacenando la estructura de ficheros en memoria,
# para copiar el contenido a su destino

# path con varios directorios

# un solo directorio








#function getseparador(  )



time.sleep( 30 )
