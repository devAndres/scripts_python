
# IMPORTO LAS LIBRERÍAS :
import time, random, string

# FUNCIONES :

# Devuelvo una palabra aleatoria, del tamaño pasado por parámetro
def randomword(length):
   return ''.join(random.choice(string.ascii_lowercase) for i in range(length))

# Imprimo por consola el tiempo (formateado) requerido para ejecutar el algoritmo
def print_process_time(text, num):
    print('\t%-21s%.8f' % (text, num))

# Lista de (10000) palabras aleatorias (grupos de 10 carácteres)
list_words = [randomword(10) for x in range(1, 10001)]

"""
#abreviado = [x.upper() for x in ['ivan', 'andres'] if x[0] == 'i']

nombres =['ivan', 'andres']
for i in nombres :
    print( i )
mayusculas = []
for i in nombres :
    mayusculas.append( i.upper() )
for i in mayusculas :
    print( i )
abreviado = [x.upper() for x in ['ivan', 'andres']]
for i in abreviado :
    print( i )
"""

# CONCATENACIÓN --------------------------------------------------------------------

print('\nConcatenación de Strings :')

# Concateno recorriendo el listado, con el bucle for e imprimo el tiempo empleado
start = time.time()
s = ''
for word in list_words:
	s += word
print_process_time('For:', time.time()-start)

# Concateno usando el método join(listado) e imprimo el tiempo empleado
start = time.time()
s = ''.join(list_words)
print_process_time('Join:', time.time()-start)


# COPIAR A NUEVO LISTADO --------------------------------------------------------------------
print('\nCopiado de listado a uno nuevo :')

# Con bucles
print('\nCon loops :')

# Copio el listado original a uno nuevo (convirtiendo el contenido a mayúsculas)
#  recorriendo el primero con un for e imprimo el tiempo empleado
start = time.time()
list_new = []
for word in list_words:
    list_new.append(word.upper())
print_process_time('For:', time.time()-start)

# List comprehensions
start = time.time()
list_new = [word.upper() for word in list_words]
print_process_time('List comprehensions:', time.time()-start)


# Con métodos :
print('\nCon métodos :')

# Nota : El método map() aplica la funcion (str.upper) a cada elemento de la lista original

# map object :
# Creo un listado de 'map object' con los elementos del listado original, convertido a mayúsculas
# map returns a 'map object'. It's possible to iterate over this list:
# <map object at 0x7fe955c05ac8>
start = time.time()
list_new = map(str.upper, list_words)
print_process_time('map:', time.time()-start)

# map object to list :
# Creo un listado, pasándole a su constructor, el método map(función, colección) e imprimo el tiempo empleado
# ['UAJOEWPZFW', 'VEAEUCKZVA', 'MYPNJMEEPG', 'YLPWLEHVNI', ...]
start = time.time()
list_new = list( map(str.upper, list_words) )
print_process_time('map-list:', time.time()-start)


# Nuevo en Python 3.5:
# ['UAJOEWPZFW', 'VEAEUCKZVA', 'MYPNJMEEPG', 'YLPWLEHVNI', ...]
start = time.time()
list_new = [*map(str.upper, list_words)]
print_process_time('*map:', time.time()-start)

# Rápido pero requiere importar
# ['UAJOEWPZFW', 'VEAEUCKZVA', 'MYPNJMEEPG', 'YLPWLEHVNI', ...]
from itertools import starmap
start = time.time()
list_new = [starmap(str.upper, list_words)]
print_process_time('starmap:', time.time()-start)
