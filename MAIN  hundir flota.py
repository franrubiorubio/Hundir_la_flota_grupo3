import numpy as np
import random 

from clases import *
from variables import *


print("Hola, va a comenzar el juego hundir la flota.")
print(" ")
print("Derrota a la máquina hundiendo todos sus barcos,\nla máquina y tu teneis 20 vidas cada uno, \n si se acierta se vuelve a disparar.")
print(" ")
print("Tablero jugador:\n ", tablero_jugador.tablero)

while tablero_jugador.vidas > 0 and tablero_maquina.vidas > 0: #utilizamos while para que se siga ejecutando el juego hasta q uno llegue a 0

    if turno == "jugador":
        print("\n--- TURNO DEL JUGADOR --- \n")

        # si acierta, sigue
        while tablero_jugador.recibir_disparo(tablero_maquina):
            print("\n¡Has acertado! Puedes volver a disparar.\n")

        print("\nFallaste. Turno de la máquina.\n")
        turno = "maquina"

    else:
        print("\n --- TURNO DE LA MÁQUINA --- \n")

        while tablero_maquina.recibir_disparos_maquina(tablero_jugador):
            print("\nLa máquina acertó y vuelve a disparar...\n")

        print("\nLa máquina falló. Tu turno.\n")
        turno = "jugador"


# FIN DE PARTIDA
print("\n --- FIN DEL JUEGO --- ")

if tablero_jugador.vidas <= 0:
    print("\n La máquina ganó.")
else:
    print("\n ¡GANASTE! Hundiste su flota.")