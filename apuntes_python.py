
"""
                PYTHON 3


https://python-para-impacientes.blogspot.com/2014/02/operaciones-con-fechas-y-horas.html


=========================================================================================================================
=========================================================================================================================
=========================================================================================================================
=========================================================================================================================
LENGUAJE :

Lenguaje interpretado
Tipado fuerte
Tipado dinámico (con cada asignación de valor)
Case sensitive



=========================================================================================================================
=========================================================================================================================
=========================================================================================================================
=========================================================================================================================
EJECUCIÓN :


Llamar al script :
    Python 2 ->     python script.py
    Python 3 ->     python3 script.py


Directivas al preprocesador :



Pasar parámetros al script :



=========================================================================================================================
=========================================================================================================================
=========================================================================================================================
=========================================================================================================================
VARIABLES :

Se puede realizar más de una asignación, en una sola línea
a = b = 10

Se puede declarar y asignar diferentes valores a varias variables
a, b, c = 10, "Hola", [1, 2, 3, 4]

La asignación de un valor a una variable, nunca copia un valor, sino que siempre asigna una referencia.
Por lo que si se asigna una elemento mutable(objetos, listas, diccionarios), la asignación de valor se hace por referencia.
si se modifica su valor original, también se ve afectado los referenciados
Las asignaciones de valores no mutables (valores literales, constantes, tuplas), si se pueden modificar individualmente
Esto se puede evitar, realizando la asignación de una copia del objeto mutable, en vez de su referencia
Para ello se utiliza el método 'deepcopy(var)' del módulo 'copy' (requiere 'import copy')
import copy
a = deepcopy( var )

del variable        # Desreferenciar la variable
type( variable )    # Devuelvo el tipo de dato de la variable ( str, int )



=========================================================================================================================
=========================================================================================================================
=========================================================================================================================
=========================================================================================================================
TIPOS de DATOS :


datetime            # fecha y hora básica
calendar            # funciones relacionadas al calendario
collections         # contenedores de datos, de alta eficiencia
heapq               # Algoritmos para pilas y colas (Heap queue algorithm)
bisect              # Algoritmos para dividir arrays
array               # Array numéricos
sets                # Colección desordenada de elementos únicos
sched               # Planificador de eventos
mutex               # Soporte para exclusiones mutuas (Mutual exclusion support)
Queque              # Clase de colas sincronizadas
weakref             # Referencias débiles (Weak references)
UserDict            # Clase envolvente para objetos de tipo diccionario
UserList            # Clase envolvente para objetos de tipo lista
UserString          # Clase envolvente para objetos de tipo string
types               # Nombres de los tipos incorporados (built-in)
new                 # Creación de objetos internos en tiempo de ejecución (
                    # Python 2.6 : ¿deprectaed?
                    # Python 3.X : usar 'type'
copy                # Operaciones de copia, profundas y no profundas (shallow y deep)
pprint              # Impresión de fechas formateadas
repr                # Altenar implementación de 'repr()' (Alternate repr() implementation)


Tipos de String :

string          # cadena da texto
re              #
struct          #
difflib         #
StringIO        #
cStringIO       #
textwrap        #
codecs          #
unicodedata     #
stringrep       #
fpformat        #





=========================================================================================================================
=========================================================================================================================
=========================================================================================================================
=========================================================================================================================
CASTING / PARSEAR :

str( valor )                           # Devuelvo cadena, a partir de parsear un valor
int( valor )
ETC

# Convertir un string, en  un 'datetime', en base a un formato :
cadenaFecha = "01-02-2019 14:00"
cadenaFormato = "%d-%m-%y %I:%m %p"
fechaHora = datetime.strptime( cadenaFecha, cadenaFormato )



=========================================================================================================================
=========================================================================================================================
=========================================================================================================================
=========================================================================================================================
OPERADORES :


ARTIMÉTICOS :
    +       Suma
    -       Resta
    *       Multiplicación
    %       División
    /       En Python 3 es decimal ¿División entera?
    //      División con decimales
    **      Exponenciación

ASINACIÓN :
    =       +=      -=      *=      /=      //=     %=
    **=         x **= 1     ->      x = x**1
    &=          x &= 2      ->      x = x & 2
    |=          x |= 3      ->      x = x | 3
    ^=          x ^= 4      ->      x = x^4
    >>=         x >>= 5     ->      x = x >> 5
    <<=         x <<= 6     ->      x = x << 6


LÓGICOS :
    and
    or
    not


PARA SECUENCIAS :
    in
    not in
    is
    is not

A NIVEL DE BITS :
    &       AND                     Defino cada bit a 1, si ambos son 1
    |       OR                      Defino cada bit a 1, si uno de ellos es 1
    ^       XOR                     Defino cada bit a 1, si Solo uno de ellos es 1
    ~       NOT                     Invierto todos los bits
    <<      Zero fill left shift    Shift left by pushing zeros in from the right and let the leftmost bits fall off
    >>      Signed right shift      Shift right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off



=========================================================================================================================
=========================================================================================================================
=========================================================================================================================
=========================================================================================================================
ESTRUCTURAS DE CONTROL :


=========================================================================================================================
CONDICIONALES


if condicion :
    instrucciones
[elif condicion :
    instrucciones]
[else :
    instrucciones]

# Si solo se va a ejecutar una instrucción, se puede escribir todo en una línea :
if condicion : sentencia

# Operador ternario
sentenciaCasoTrue condicion else sentenciaCasoFalse



=========================================================================================================================
BUCLES :

WHILE :

while condicion :
    instrucciones
    [ if condicion :        # Salir del bucle
        break ]
    [ if condicion :        # Continuar con la siguiente iteración
        continue ]


FOR LOOPS :

# También se pueden usar las sentencias 'break' y 'continue'

for i in cadena :               # Recorro una cadena, char a char
for i in coleccion :            # Recorro los elementos de un elemento iterable

# El método 'range()' devuelve una secuencia numérica (por defecto iniciada en 0 e incrementada en 1)
for i in range( 6 ) :           # valores 0 a 5
for i in range( 5, 10 ) :       # valores 5 a 9
for i in range( 3, 10, 3 )      # valores 3-6-9

# Los FOR, pueden tener un 'else' final, que contendrá código que se ejecutará una vez finalizado el bucle


=========================================================================================================================
=========================================================================================================================
=========================================================================================================================
=========================================================================================================================
FUNCIONES :

Definir :

def nombreFuncion( [parametros[=valorPorDefecto]] ):
    instrucciones


Llamar :
    nombreFuncion(  [parametros] )


Notas :
- Los parámetros, se definen como :
    nombreFuncion( par1, par2, par3, ... )
- Los valores por defecto, se definen como :
    nombreFuncion( par1=val1, par2=val2, par3=val3, ...  )
- Para pasar una lista como parámetros :
    lista = [ "uno", "dos", "tres" ]
    nombreFuncion( lista )
- Para devolver un valor :
    return valor


FUNCIONES LAMBDA :



=========================================================================================================================
=========================================================================================================================
=========================================================================================================================
=========================================================================================================================
MÉTODOS CON STRINGS


    Se puede usar comillas "dobles" o 'simples'     ¿¿ Diferencias ??
    Si se definen entre '3 comillas simples o dobles', pueden contener comillas y lineas en blanco

    Los métodos de string, no cambian el valor original.
    Crean uno nuevo, que hay que asignárselo al string correspondiente.

    Es más eficiente usar utilizar formatos, que concatenar.


BÁSICAS :

len( cadena )                           # Devuelvo nº de chars de la cadena
cadena.count( 'string buscado' )        # Devuelvo nº de apariciones de la subcadena, en la cadena

IDENTIFICACIÓN :
cadena.isdigit()        # Devuelvo boleano, en función de si contiene solo números (sin espacios, ni punto decimal)
cadena.isalnum()        # Devuelvo boleano, en función de si es alfanumérica (letras y números, sin espacios)
cadena.isalpha()        # Devuelvo boleano, en función de si es alfabética (sin número ni espacios)
cadena.islower()        # Devuelvo boleano, en función de si solo contiene  minúsculas
cadena.isupper()        # Devuelvo boleano, en función de si solo contiene mayúsculas
cadena.isspace()        # Devuelvo boleano, en función de si solo contiene espacios en blanco


MODIFICACIÓN :
cadena.join( '====' )                   # Concatena ?????
cadena.split( 'separador' )             # Devuelvo Lista, a partir de dividir la cadena en base al separador
cadena.partition( 'separador' )         # Devuelvo Tupla, a partir de dividir la cadena en base al separador
cadena.replace( 'buscado', 'sustituto', numSustituciones? )

BÚSQUEDAS :
cadena.find( 'string buscado' )         # Devuelvo la posición de la subcadena en la cadena (-1 si no encuentro)
cadena.startsWith( "buscado" )          # Devuelvo boleano, en función de si la cadena empieza con la subcadena
cadena.endsWith( "buscado" )            # Devuelvo boleano, en función de si la cadena acaba con la subcadena

FORMATEOS :

cadena.upper()                              # Devuelco cadena convertida a mayúscula
cadena.lower()                              # Devuelco cadena convertida a minúscula

# Devuelvo cadena, eliminando espacios, \t, \n, \r
cadena.rstrip()                             # Eliminando a la derecha
cadena.lstrip()                             # Eliminando a la izquierda
cadena.strip( 'caracteres a borrar' )       # Eliminando los caracteres que estén en la subcadena

ACCESO A PARTES DE UNA CADENA (substring) :
Nota : La coordenada final, es no inclusiva.
cadena = 'Andrés'

cadena[0]               # 'A'       # Devuelvo un char (N) de la cadena

cadena[0:4]             # 'And'     # Devuelvo subcadena con los chars, desde la pos 0 a la 4
cadena[:4]              # 'And'     # Devuelvo subcadena con los chars, desde la pos 0 a la 4

cadena[2:4]             # 'dr'      # Devuelvo subcadena con los chars, desde la pos 2 a la 4

cadena[4:leng(cadena)]  # 'és'       # Devuelvo subcadena con los chars, desde la pos 4 al final de la cadena
cadena[4:]              # 'és'       # Devuelvo subcadena con los chars, desde la pos 4 al final de la cadena

cadena[:-3]             # 'and'     # Devuelvo subcadena con los chars, desde la pos 0 a la 3 (todo, menos los 3 últimos chars)







=========================================================================================================================
=========================================================================================================================
=========================================================================================================================
=========================================================================================================================
COLECCIONES :




TUPLAS ******************************************************************************************************************

    No permite cambiar el contenido de sus elementos
    Una vez creada, no se puede añadir elementos
    Los elementos no pueden ser borrados

tupla = elemento1, elemento2, ...
print( tupla[0] )


LISTADOS ******************************************************************************************************************

    Permite elementos repetidos
    Se mantiene el orden de entrada de los elementos

l = ['s', 'd', 's']
l.append('g')
l.insert( pos, 'h' )
l.remove('g')
l.pop()         #elimino y devuelvo el último elemento
l.pop( index )  #elimino y devuelvo el objeto de la posicion 'index'
del l[ index ]  #remuevo el elemento nº 'index', de la lista
del l   #elimino la lista, incluyendo su declaración
l.clear()   #vacío la lista
l.extend( l2 ) # uno la lista l2 a la lista l
l.index( 'g' )  #devuelvo el índice del elemento pasado por parámetro
l.count( 'g' )  #devuelvo el nº de elementos que contienen el valor pasado por parámetro
l.reverse() #invierto el orden de los elementos
l.sort( cmp=None, key=None, reverse=False ) #ordeno la lista ¿¿parámetros??
del l[ : ]  #borro todos los elementos
copia = l[:]  #devuelvo una copia de la lista


DICCIONARIO **************************************************************************************************************

    Desordenado
    No permite elementos repetidos

d = {'s': 3, 'd': 2, 'a': 3}
d['d'] = 3

d2 = d.copy()
d.clear()
d.get( clave )  # devuelvo el valor correspondiente a la clave. Si no, None
d.pop( clave )  #elimino el elemento y devuelvo su valor

d = dict( zip(coleccion1, coleccion2) ) #Creo un diccionario, a partir de 2 colecciones (q tengan el mismo nº de elementos)
d.items() #Devuelvo una colección de tuplas, con 2 campos (key-value)
d.keys() #Devuelvo una colección de tuplas, con las claves
d.values() #Devuelvo una colección de tuplas, con los valores
d = dict.fromkeys( coleccion, valor ) #devuelvo un diccionario con las claves contenidas en la colección, y les asigno el valor pasado por parámetro (si no, None)
d.update( d2 )  #actualizo el dic. con el dic. pasado por parámetro. Actualizo los valores preexistentes, añado el restoS


SET / CONJUNTO ***********************************************************************************************************

    No permite elementos repetidos
    No permite elementos mutables (listas, matrices, etc)
    No mantiene el orden de entrada de los elementos

l = set()
l.add('g')
l.discard('g')  # eliminio
l.remove('g')   # elimino. Si no existe lanza KeyError



if 'g' in l:
    print('existe')


=========================================================================================================================
=========================================================================================================================
=========================================================================================================================
=========================================================================================================================
DIRECTORIOS y FICHEROS :



Librerías :
    OS          # Requiere import os
    OS.path     # Requiere import os.path
    shutils     # Requiere import shutil


Se puede utilizar comodines :
.       Directorio actual.
..      Directorio padre



os.getcwd()             # Devuelvo el Current Working Directory (Unicode para Python 3.X)
os.getcwdu()            # En Python 2.X, devuelve en formato Unicode
os.listdir( path )      # Devuelvo Lista con los archivos y carpetas contenidas en el path
                        # Python 2.X -> Si se le pasa un objeto Unicode, los items recibidos, mantienen esa codificación, si es posible
                        # Python 3.X -> Permite especificar directorio de tipo bytes


DIRECTORIOS y FICHEROS ***********************************************************************************************************

os.path.exists( path )                              # Devuelvo booleano, en función de si existe o no
os.rename( nAntiguo, nNuevo )                       # Cambio el nombre a un directorio/fichero
                                                    # Si nNuevo ya existe :
                                                    #       Si es un directorio, lanza excepción OSError
                                                    #       Si es un fichero, lo machaco
shutil.move( pathOrigen, pathDestino )              # Muevo un fichero/directorio


DIRECTORIOS ***********************************************************************************************************

os.path.isdir( path )                               # Devuelvo booleano, en función de si es un directorio
os.mkdir( path, [permisos] )                        # Creo un directorio, en una ruta existente
                                                    # Python 3.4 :
                                                        from pathlib import Path
                                                        path = Path( 'diarA/dirB/dirC' )
                                                        path.mkdir( parents=True )
os.mkdirs( path, [permisos], [exist_ok=True] )      # Creo directorios, recursivamente
                                                    # 'Permisos' (solo algunos SO), por defecto : Todas las operaciones
                                                    #       0o777   Todas las operaciones
                                                    #       0o444   Solo lectura
                                                    # Python 3.2 :
                                                    # exist_ok=True : Si no existe algún directorio del path, lo creo

os.rmdir( nDirectorio )                             # Borro directorio
os.removedirs( pathCompleto )
                                                    # Borrar un directorio no vacío, lanza excepción OSError
shutil.rmtree( nDirectorio )                        # Borro directorio no vacío
shutil.copytree( "dirA.ext", "dirB.ext" )           # Copio el directorio (No vacío) A, como B,
os.path.join( dirA, dirB, dirC )                    # Devuelvo una cadena con un path obtenido con los parámetros

FICHEROS ***********************************************************************************************************

os.path.ispath( path )                                  # Devuelvo booleano, en función de si es un directorio
os.remove( "archivo.ext" )                              # Borrar fichero
shutil.copy( "ficheroA.ext", "ficheroB.ext" )           # Copio el fichero A, como B
shutil.copy2( "ficheroA.ext", "ficheroB.ext" )          # Copio el fichero A, como B, incluyendo metadatos
shutil.copystat( "ficheroA.ext", "ficheroB.ext" )       # Copio el fichero A, como B, incluyendo metadatos
shutil.copymode( "ficheroA.ext", "ficheroB.ext" )       # Copio el fichero A, como B, incluyendo permisos



=========================================================================================================================
=========================================================================================================================
=========================================================================================================================
=========================================================================================================================
CONSOLA :

print( "un texto" )                         # Muestro un texto en consola, seguido de 'salto de línea'
print( "un texto", end=" " )                # Parámetro opcional : cadena para sustituir el 'salto de línea' final

print( f"N es igual a {n}" )                # Muestro un texto con variables en consola

leido = input()                             # Leo un string por teclado
leido = input( "Escribe :" )                # Muestro un texto en consola y Leo un string por teclado

NOTAS sobre la entrada por teclado :
- Para operar con valores numéricos leídos por teclado, primero hay que parsearlos de string, a su correspondiente tipo.
- La conversion, se puede hacer dentro de un bloque 'try' para controlar posibles excepciones de tipo 'ErrorValue'


os.system( "cls" )      # Limpio la consola en Windows
os.system( "clear" )    # Limpio la consola en Unix

Ejemplo de limpieza de pantalla multiplataforma :
# SOs Windows
if os.name == "ce" or os.name == "nt" os.name == "dos"  :
    os.system( "cls" )
# SOs Unix
if os.name == "posfix" :
    os.system( "clear" )





=========================================================================================================================
=========================================================================================================================
=========================================================================================================================
=========================================================================================================================
FECHAS :

from datetime import datetime, date, time, timedelta
import calendar


DATE - FECHA :

fecha = date(  )                            # Creo fecha concreta
fecha2 = fecha + timedelta( days=2 )        # Fecha + 2 días
fecha = date.today()                        # Fecha actual
diferenciaDias = fecha - fecha2


TIME - HORA :

hora = time( 10, 5, 0 )             # Creo una horra concreta (Horas, Minutos y Segundos)


DATETIME - FECHA y HORA :

fechaHora = datetime.now()
fechaHora.utcnow()
fechaHora.day
fechaHora.month
fechaHora.year
fechaHora.hour
fechaHora.minute
fechaHora.second
fechaHora.microsecond
fechaHora = datetime.today()        # Fecha en formato ISO 8601


MÁSCARAS - FORMATEO :

# Ejemplo :
patronFormato = "%d-%m-%y %I:%m %p"
fechaHora = datetime.today()
fechaHoraFormateada = fechaHora.strftime( patronFormato )

Claves que se pueden combinar para aplicar distintos formatos :

%c  Representación local de fecha y hora
%x  Fecha local
%X  Hora local

%a  Nombre local abreviado de Dia de la Semana
%b  Nombre local abreviado de Dia del mes

%A  Nombre local completo de Dia de la Semana
%B  Nombre local completo del Mes

%d  Día del Mes (01-31)
%j  Día del Año (001-366)

%W   Semana del año (00-53) - Domingo es el primer día
%w   Defino el primer día de la semana (0:Domingo, 1:Lunes, ...)

%m  Mes (01-12)

%y  Año en formato corto
%Y  Año en formato largo

%H  Hora 24h (00-23)
%I  Hora 12h (01-12)
%M  Minuto (00-59)
%S  Segundo (00-59)
%p  Etiqueta AM/PM

%Z Nombre de la zona horaria


=========================================================================================================================
=========================================================================================================================
=========================================================================================================================
=========================================================================================================================
CONTROLAR EXCEPCIONES :

Requiere 'import errno'

Ejemplos :

1º Controlar la excepción lanzada, al intentar crear un directorio que ya existe :

try:
    os.mkdir( nDirectorio )
except OSError as e:
    if e.errno != erno.EEXISTS:
        raise

2º Controlar la excepción lanzada, al intentar crear un directorio en una ruta, especificando en el path alguna carpeta inexistente

try:

except OSError as e:




3º Controlar la excepción lanzada, al intentar (¡¡¡¡Que no se ha parseado el tipo de dato!!!!)
try:

except ValueError :
    print( "Valor incorrecto introducido !" )





****************************************************************

os.chdir( path )            # Me situo el en directorio indicado ( como 'cd path' en el SO )
os.system( comandoSO )      # Ejecuto un comando del SO
dir( objeto )               # Muestro las propiedades y métodos del objeto, sin sus valores

# Imprimir todas las keywords de Python :
import keyword
print( keyword.kwlist )

# Imprimir todos los built-in :
import builtins
print( dir( builtins ) )


****************************************************************

CLASES :

Ejemplo :

class Persona :
        nombre="Andres"
        edad = 29
    def saludar() :
        print( f"Hola soy {nombre} !" )
    def hablar( frase ) :
        print( frase )




=========================================================================================================================
=========================================================================================================================
=========================================================================================================================
=========================================================================================================================
LIBRERÍA MATH :

math.isnan( variable )          # Devuelvo booleano, en función de si No es un número



=========================================================================================================================
=========================================================================================================================
=========================================================================================================================
=========================================================================================================================
FICHEROS :

Modos de Acceso :
    r       lectura         Si el fichero no existe, devuelvo error
    a       append          Si el fichero no existe, lo creo
    w       escribir        Si el fichero no existe, lo creo
    x       crear           Si el fichero ya existe, devuelvo error ''

Como se va a tratar el fichero :
    t       texto       Modo texto
    b       binario     Modo binario (imagenes, etc)

Si tras usar un fichero, no se cierra, pueden perderse los cambios realizados.

Para eliminar ficheros y directorios, hay que importar el modulo OS y utilizar sus funciones.



=========================================================================================================================
LECTURA :

fichero.read()                  # Leo todo el contenido del fichero
fichero.read( num_chars )       # Leo solo un número concreto de chars
fichero.readline()              # Leo solo una línea (Leo una, por cada vez que llame a la función)


# Ejemplo : leo un fichero (línea a línea) y lo imprimo por consola
fichero = open( nombreFichero, modoAcceso )
for linea in fichero :
    print( fichero.readline )
fichero.close()

=========================================================================================================================
ESCRITURA :

Parámetros opcionales para la lectura/escritura de ficheros, definen la codificación del texto.

    encoding='ISO-8859-1'
    encoding='mac_roman'



# Ejemplo : Abro un fichero y Escribo una línea en un fichero
fichero.open( nombreFichero, modoAcceso )
fichero.write( "Esto es una línea" )
fichero.close()

# Ejemplo con lista

lista_lineas = [
    "",
    "",
    ""
]
with open(FILE_OUPUT, 'w') as fichero :
    for linea in lista_lineas :
        f.write('%s\n' % linea)


# Ejemplo con diccionario
diccionario = {
    '' : '',
    '' : '',
    '' : ''
}
with open(FILE_OUPUT, 'w') as f:
    for dni, nombre in users.items():
        f.write('%s - %s\n' % dni, user)




=========================================================================================================================
=========================================================================================================================
=========================================================================================================================
=========================================================================================================================
LIBRERÍAS :


NÚMEROS :
numbers         # Clases base abstractas numéricas
math            # Funciones matemáticas
cmath           # Funciones matemáticas para números complejos
decimal         # Aritmética decimal fija y de punto flotante (Decimal fixed point and floating point arithmetic)
fractions       # Números racionales
random          # Generar números pseudo-aleatorios
itertools       # Funciones para crear iteradores para bucles eficientes
functools       # Funciones y operaciones de orden superior en objetos llamables
                # higher-order functions : Funciones de orden superior : reciben una ecuación de entrada y tienen una ecuación de salida
operator        # Operadores estándar como funciones

FICHEROS y DIRECTORIOS :
os.path         # Manejo de rutas comunes
fileinput       # Iterar entre líneas, entre diferentes flujos de entrada
stat            # Interpretar los resultados de 'stat()'
statvfs         # Constantes usadas con 'os.statvfs'
filecmp         # Comparación de ficheros y directorios
tempfile        # Generar ficheros y directorios temporales
linecache       # Acceso aleatorio a líneas de texto
shutil          # Operaciones de alto-nivel con ficheros
dircache        # Listar directorios cogidos (catched)
glob            # Expansión de patrones de rutas de estilo Unix
fnmatch         # Búsqueda de patrones de directorios de estilo Unix
macpath         # Funciones para el manejo de rutas de Mac OS 9

PERSISTENCIA de DATOS :
pickle          # Serializzación de objetos Python
cPickle         # Versión más rápida de 'pickle'
copy_reg        # Funciones de soporte de registro de 'pickle' (Register pickle support functions)
shelve          # Persistencia de objetos Python
marshal         # Serialización interna de objetos Python
andydbm         # Acceso genérico a
whichdb         #
dbm             #
gdbm            #
dbhash          #
bsddb           #
dumbdm          #
dumbdbm         #
sqlite3         #


NOTA sobre 'dbm' :
    BBDD estilo DBM : BBDD que usa cadenas de texto, como keys de las tablas
    dmb : Front-end para BBDD de estilo DBM.
    1º Se usa wichdb() para identificar para identificar las BBDD
    2º Se abren con el módulo adecuado
    3º Como Back-end, se usa 'shelve' (que almacena objetos en una BBDD, usando 'pickle')

COMPRESIÓN y ARCHIVADO de DATOS :
zlib            # Compresión compatible con 'gzip'
gzip            # Soporte para ficheros 'gzip'
bz2             # Conversión compatible con 'bzip2'
zipfile         # Trabajar con ficheros 'zip
tarfile         # Leer y escribir ficheros 'tar'

FORMATOS de FICHEROS :
csv                 # Leer y escribir ficheros CSV
ConfigParser        # Configuración de parseo de ficheros
robotparser         # Parseador para robots.txt
netrc               # Procesamiento de ficheros netrc
xdrlib              # Codificar y decodificar datos XDR
plistlib            # Generar y parsear ficheros '.plist' de Mac OS X

CRIPTOGRAFÍA :
hashlib             # Registros criptográficos seguros y resumir mensajes
hmac                # Registro criptográfico con clave, para autentificación de mensajes
md5                 # Algorítmo para resumen de mensajes MD5
sha                 # Algorítmo para resumen de mensajes  SHA-1




=========================================================================================================================
=========================================================================================================================
=========================================================================================================================
=========================================================================================================================
Librerías para implementar Interfaces Gráficas :



Tkinter ==================================================================================================================

Basada en la lib. gráfica 'TCL/TK'
Preinstalada con Python (si no : apt-get install python3-tk)
Multiplataforma

Ventajas :

Desventajas :


WxPython ==================================================================================================================

Basada en la lib. gráfica 'WxWidgetss'

Ventajas :

Desventajas :


PyQT ==================================================================================================================

Basada en la lib. gráfica 'C++ QT (KDE)'

Ventajas :

Desventajas :


PyGTK ==================================================================================================================

Basada en la lib. gráfica 'C GTK (GNOME)'

Ventajas :

Desventajas :







"""
