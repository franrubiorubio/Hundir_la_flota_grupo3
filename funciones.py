
import numpy as np
from variables import *
from clases import Tablero

def mostrar_tablero(tablero):
    """Imprime un tablero bonito en consola"""
    print("   " + " ".join(str(i) for i in range(TAMANO)))
    for i in range(TAMANO):
        fila = [tablero[i,j] if tablero[i,j] != "" else "." for j in range(TAMANO)]
        print(f"{i:2} " + " ".join(fila))

