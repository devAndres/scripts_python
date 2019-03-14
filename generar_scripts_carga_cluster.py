# -*- coding: utf-8 -*-

TIPO_CONTROLADOR = 4
TIPO_PROVINCIA = 2
TIPO_NODO = 3

registros = []

fichero = 'controladores.csv'
primera_linea = True
with open(fichero, 'r') as entrada :
    for linea in entrada :
        campos = linea.strip().split(';')
        if primera_linea:
            primera_linea = False
            continue
        registros.append("VALUES('%s', '%s', %s, %s),\n" % (campos[1], campos[1], TIPO_CONTROLADOR, True if campos[5]==1 else False))

fichero = 'provincias_zonas.csv'
primera_linea = True
with open(fichero, 'r') as entrada :
    for linea in entrada :
        campos = linea.strip().split(';')
        if primera_linea:
            primera_linea = False
            continue
        registros.append("VALUES('%s', '%s', %s, %s),\n" % (campos[1], campos[2], TIPO_PROVINCIA, True if campos[3][-3:]=='_RS' else False))

fichero = 'nodos.csv'
primera_linea = True
with open(fichero, 'r') as entrada :
    for linea in entrada :
        campos = linea.strip().split(';')
        if primera_linea:
            primera_linea = False
            continue
        registros.append("VALUES('%s', '%s', %s, %s),\n" % (campos[0], campos[0], TIPO_NODO, True if campos[1]>1 else False))

fichero = 'registros_procesados.txt'
with open(fichero, 'w') as salida :
    salida.write( "INSERT INTO public.clusters (code, name, cluster_type_id, ransharing)\n" )
    for linea in registros :
        salida.write(linea)
