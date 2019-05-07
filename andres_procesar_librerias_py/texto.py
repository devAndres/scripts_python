

#   Andrés Fernández Burón
#
#   andres_develops@outlook.es
#   Mayo 2019





#   Importo librerías :




#
#   MÉTODOS :
#
#
#   normalizar_texto( texto )
#
#   rellenar_linea( linea, caracter, sentido )










# Devuelvo un String formateado (sin acentos, eñe, etc)
# ¿¿  No hace falta, porque ya leo los ficheros, en codificación 'ISO-8859-1'  ??
"""def normalizar_texto( texto ) :
    texto_normalizado = ""
    for i in range( 0, len( texto ) ) :
        if texto[i] == 'á' :
            texto_normalizado = texto_normalizado + 'a'
        elif texto[i] == 'Á' :
            texto_normalizado = texto_normalizado + 'A'
        elif texto[i] == 'é' :
            texto_normalizado = texto_normalizado + 'e'
        elif texto[i] == 'É' :
            texto_normalizado = texto_normalizado + 'E'
        elif texto[i] == 'í' :
            texto_normalizado = texto_normalizado + 'i'
        elif texto[i] == 'Í' :
            texto_normalizado = texto_normalizado + 'I'
        elif texto[i] == 'ó' :
            texto_normalizado = texto_normalizado + 'o'
        elif texto[i] == 'Ó' :
           texto_normalizado = texto_normalizado + 'O'
    return texto"""






# Relleno una línea, con un caracter, en un sentido concreto (hasta el ancho definido por la variable global 'ancho_consola')
#
#   Posibles sentidos :
#          -1       Por la izquierda de la línea
#           0       A ambos lados de la línea
#           1       Por la derecha de la línea
#
def rellenar_linea( linea, caracter, sentido ) :
    tam_linea = leng( linea )
    linea = "  " + linea + "  "
    if sentido not in range( -1, 1 ) :
        print( "El sentido definido para rellenar la línea, es incorrecto" )
        print( "Uso 'rellenar por la derecha', por defecto" )
        sentido = 1
    else :
        # Izquierda
        if sentido == -1 :
            linea.rstrip()
            for i in range( tam_linea+1, tam_linea ) :
                linea = caracter + linea
        # Centro
        elif sentido == 0 :
            if len(linea) % 2 != 0 :
                ANCHO_CONSOLA += 1
            ancho_aux = ( ANCHO_CONSOLA - (  tam_linea + 2 ) ) // 2
            for i in range( 0, ancho_aux ) :
                linea = caracter + linea
            for i in range( 0, ancho_aux ) :
                linea += caracter
        # Derecha
        elif sentido == 1 :
            linea.lstrip()
            for i in range( ancho_consola-(tam_linea+1), 0 ) :
                linea += caracter
    return linea
