from clases import Tablero
from funciones import mostrar_tablero
from variables import TAMANO
import random

print("🚢 Bienvenido a Hundir la Flota 🚢")

# Inicializar tableros
jugador = Tablero("Jugador")
maquina = Tablero("Máquina")
jugador.inicializar_barcos()
maquina.inicializar_barcos()

turno_jugador = True
juego_activo = True

while juego_activo:
    if turno_jugador:
        print("\n Tu tablero:")
        mostrar_tablero(jugador.tablero_barcos)
        print("\n Tablero enemigo:")
        mostrar_tablero(maquina.tablero_disparos)
        try:
            fila = int(input("Fila (0-9): "))
            col = int(input("Columna (0-9): "))
            resultado = maquina.recibir_disparo((fila, col))
            print(resultado)
            if resultado == "Agua":
                turno_jugador = False
        except:
            print("Introduce coordenadas válidas.")
    else:
        # Turno de la máquina
        while True:
            fila, col = random.randint(0, TAMANO-1), random.randint(0, TAMANO-1)
            resultado = jugador.recibir_disparo((fila, col))
            if resultado != "Ya disparado aquí":
                print(f"La máquina dispara en ({fila},{col}): {resultado}")
                if resultado == "Agua":
                    turno_jugador = True
                break

    # Comprobar si alguien ha ganado
    if jugador.barcos_restantes() == 0:
        print("💀 Has perdido. La máquina ha hundido todos tus barcos.")
        juego_activo = False
    elif maquina.barcos_restantes() == 0:
        print("🏆 ¡Has ganado! Hundiste todos los barcos enemigos.")
        juego_activo = False