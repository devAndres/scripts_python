



# Obtengo el carácter que separa las partes del path
def getPartesPath() :
    if path_entrada != "" :
        partes_path = path_entrada.split( '/' )
        if len(partes_path) > 0 :
            separador_path = '/'
        else :
            partes_path = path_entrada.split( '\\' )
            if len(partes_path) > 0 :
                separador_path = '\\'
            else :
                separador_path = '/'
        print( "El separador de path es %s" % separador_path )
        return separador_path



# Compruebo si es un Fichero o si es un Directorio
#partes_path = path_entrada.split( '.' )
def esDirectorio() :
    if path_entrada.find('.') != -1 and path_entrada.find('.') > path_entrada.find(separador_path) :
        print( 'Es un fichero', end='' )
    else :
        print( 'Es un directorio', end='' ) #o un fichero sin extensión' )


# Compruebo si es un Fichero o si es un Directorio
#partes_path = path_entrada.split( '.' )
def esFichero() :
    if path_entrada.find('.') != -1 and path_entrada.find('.') > path_entrada.find(separador_path) :
        print( 'Es un fichero', end='' )
    else :
        print( 'Es un directorio', end='' ) #o un fichero sin extensión' )


# Compruebo si está en una ruta o no (directorio actual)
def esUbicaciónActual() :
    if path_entrada.count( separador_path ) == 0 :
        print( ' dentro el directorio actual' )
    else :
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




