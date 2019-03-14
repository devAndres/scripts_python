# -*- coding: utf-8 -*-

FICHEROS = [
    'area_controlador.csv',
    'zona_area.csv',
    'zona_controlador.csv',
]

FICHERO_SALIDA = 'generar_scripts_relaciones_entre_clusters.txt'
FICHERO_CLUSTERS = '_clusters.csv'

# Obtengo las correspon de nombre de cluster con su id
clusters_id = {}
primera_linea = True
with open (FICHERO_CLUSTERS,'r' ) as f :
    for linea in f:
        tupla = linea.strip().split(';')
        if primera_linea :
            primera_linea = False
            continue
        clusters_id[tupla[1]] = tupla[0]

# Obtengo las lineas de los ficheros de entrada
registros = []
for fichero in FICHEROS :
    primera_linea = True
    with open( fichero, 'r' ) as f :
        for linea in f :
            padre, hijo = linea.strip().split(';')

            if primera_linea :
                primera_linea = False
                continue

            padre_id = None
            hijo_id = None

            if padre in clusters_id: padre_id = clusters_id[padre]
            if hijo in clusters_id: hijo_id = clusters_id[hijo]

            if padre_id != None and hijo_id != None:
                registros.append('(%s, %s),' % (padre_id, hijo_id))
            else:
                print('Alguno de los campos no tiene clave registrada: %s, %s' % (padre, hijo))


            """
            registro = []
            for i in campos :
                for k,v in clusters_id.items() :
                    if k == i :
                        registro.append(v)
                if len(registro) == 2 :
                    registros.append('%s;%s' % (registro[0], registro[1]))
                else :
                    print('Alguno de los campos de %s, no tiene clave registrada' % campos)
            """

# Creo el fichero de salida
with open(FICHERO_SALIDA, 'w') as f:
    f.write('INSERT INTO public.cluster_level (parent_id, child_id) VALUES\n')
    for i in registros :
        f.write('%s\n' % i)
