#!/usr/bin/python
# -*- coding: utf-8 -*-


from Tkinter import *
from tkMessageBox import *


def preguntar() :
    showerror( "Esto es una pregunta. Quieres salir ?" )

def get_respuesta() :
    if askyesno( "Verificación", "Realmente quieres salir ?" ) :
        showwarning( "Si", "No implementado" )
    else :
        showwarning( "No", "Cancelado" )

Button( text="Salir", command = get_respuesta ).pack( fill=X )
Button( text="Pregunta", command=preguntar ).pack( fill=X )
mainloop()
