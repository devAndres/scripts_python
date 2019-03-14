# -*- coding: utf-8 -*-

FICHERO_CLUSTERS = '_clusters.csv'
FICHERO_CELDAS = '_celdas.csv'

FICHERO_ENTRADA = 'celdas.csv'
FICHERO_SALIDA = '_celdas.txt'

# Obtengo las correspondencias cluster-ID
clusters_id = {}
primera_linea = True
with open (FICHERO_CLUSTERS,'r' ) as f:
    for linea in f:
        tupla = linea.strip().split(';')
        if primera_linea :
            primera_linea = False
            continue
        clusters_id[tupla[1]] = tupla[0]

# Obtengo las correspondencias celda-ID
celdas_id = {}
primera_linea = True
with open (FICHERO_CELDAS,'r' ) as f:
    for linea in f:
        tupla = linea.strip().split(';')
        if primera_linea :
            primera_linea = False
            continue
        celdas_id[tupla[1]] = tupla[0]

# Leo
registros = []
primera_linea = True
with open( FICHERO_ENTRADA, 'r' ) as f:
    for linea in f :
        linea = linea.strip().replace('"', '')
        celda, _, tech, area, zona, _, nodo = linea.split(';')

        if primera_linea :
            primera_linea = False
            continue

        id_celda, id_area, id_zona, id_nodo = '', '', '', ''

        if celda in celdas_id : id_celda = celdas_id[celda]
        if zona in clusters_id : id_zona = clusters_id[zona]
        if area in clusters_id : id_area = clusters_id[area]

        if tech != '4g':
            if nodo in clusters_id: id_nodo = clusters_id[nodo]

        if id_celda == '': print('La celda %s no tiene ID registrada' % celda)
        if id_zona != '': registros.append('(%s, %s),' % (id_zona, id_celda))
        else: print('La zona %s no tiene ID registrada' % zona)
        if id_area != '':  registros.append('(%s, %s),' % (id_area, id_celda))
        else: print('El area %s no tiene ID registrada' % area)
        if tech != '4g' and id_nodo != '' : registros.append('(%s, %s),' % (id_nodo, id_celda))
        else: print('El nodo 2/3G %s no tiene ID registrada' % nodo)

# Salida a fichero
with open( FICHERO_SALIDA, 'w') as f :
    for i in registros:
        f.write( '%s\n' % i )
