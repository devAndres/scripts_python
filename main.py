
"""
                PYTHON


****************************************************************

Strings
    Mejor usar utilizar formatos, q concatenar
    Si se definen entre '3 comillas simples o dobles', pueden contener comillas y lineas en blanco



****************************************************************

TUPLAS
    No permite cambiar el contenido de sus elementos
    Una vez creada, no se puede añadir elementos
    Los elementos no pueden ser borrados

tupla = elemento1, elemento2, ...
print( tupla[0] )



****************************************************************

LISTADO
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


****************************************************************

DICCIONARIO desordenado
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

****************************************************************

SET / CONJUNTO
    No permite elementos repetidos
    No permite elementos mutables (listas, matrices, etc)
    No mantiene el orden de entrada de los elementos

l = set()
l.add('g')
l.discard('g')  # eliminio
l.remove('g')   # elimino. Si no existe lanza KeyError



if 'g' in l:
    print('existe')

"""


FILE_INPUT = "datos.csv"
FILE_OUPUT = "datos_procesado.csv"

users = {}
colores = set()

with open(FILE_INPUT, 'r') as f:
    for line in f:
        line = line.strip()
        #primer_valor, delimitador, resto =  line.partition(';')
        name, _, color_pelo = line.split(';')
        users[name] = {'nombre': name, 'color_pelo': color_pelo}
        colores.add(color_pelo)

"""

for user, data in users.items():
    print(user)
    print(data)


for user in users:
    print('Usuario: %s' % user)
    print('Usuario: %s    Color pelo: %s' % (user, users[user]['color_pelo']))

    print('EL usuario {a} le gusta mucho el nombre {a} porque es {moreno}'.format(
        a=user,
        moreno=users[user]['color_pelo']
    ))

    print('EL usuario {0} le gusta mucho el nombre {1} porque es {2}'.format(
        user,
        user,
        users[user]['color_pelo']
    ))
"""


#print(colores)

with open(FILE_OUPUT, 'w') as f:
    for user, data in users.items():
        f.write('%s\n' % user)




import csv


