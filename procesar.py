# -*- coding: utf-8 -*-

import csv

FICHERO_CELDAS = 'celdas.csv'
FICHERO_CONTROLADORES = 'controladores.csv'
FICHERO_SALIDA = 'salida.csv'

# Leo los controladoros
controladores = {}
with open(FICHERO_CONTROLADORES, 'r') as f:
    for linea in f:
        _id, _nombre = linea.strip().split( ';' )
        controladores[_id] = _nombre

# Leo las celdas
celdas = []
with open(FICHERO_CELDAS, 'r') as f:
    for linea in f:
        data = linea.strip().split( ';' )
        celdas.append({
            'nombre': data[0],
            'id_controlador': data[2],
            'controlador': controladores[data[2]] if data[2] in controladores else '',
        })

# Creo el fichero de salida
with open(FICHERO_SALIDA, "w") as f:
    campos = ['nombre', 'controlador', 'id_controlador']
    writer = csv.DictWriter(f, fieldnames=campos)
    writer.writeheader()
    for celda in celdas:
        writer.writerow(celda)




"""
lineas = []


with open(fichero_csv, 'r') as f:
    for linea in f:
        num_celda, empresa, tecnologia, controlador, otro = linea.strip().split( ';' )

        if tecnologia == '3g' :
            controlador = 'RNC' + controlador

        elif tecnologia == '2g' :
            controlador = 'BSC_H_1'

        lineas.append([
            num_celda, empresa, controlador, otro
        ])




with open(datos_procesados, 'w') as f:
    for linea in lineas :
        f.write('%s\n' % ';'.join(linea))
        f.write('%s;%s;%s;%s\n' % (linea[0], linea[1], linea[2] , linea[3]))

"""



