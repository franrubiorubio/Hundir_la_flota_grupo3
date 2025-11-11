import numpy as np
import random
from variables import *

class Tablero:
    def __init__(self, id_jugador):
        self.id_jugador = id_jugador
        self.tablero_barcos = np.full((TAMANO, TAMANO), AGUA)  # Lo que tiene el jugador
        self.tablero_disparos = np.full((TAMANO, TAMANO), AGUA) # Lo que vemos de disparos
        self.barcos = BARCOS

    def colocar_barco(self, barco):
        """Intenta colocar un barco en el tablero"""
        tablero_temp = self.tablero_barcos.copy()
        for fila, col in barco:
            if fila < 0 or fila >= TAMANO or col < 0 or col >= TAMANO:
                return False
            if tablero_temp[fila, col] == BARCO:
                return False
            tablero_temp[fila, col] = BARCO
        self.tablero_barcos = tablero_temp
        return True

    def crear_barco_aleatorio(self, eslora):
        """Crea un barco aleatorio de eslora dada"""
        for intento in range(100):
            barco = []
            fila, col = random.randint(0, TAMANO-1), random.randint(0, TAMANO-1)
            orientacion = random.choice(["N","S","E","O"])
            barco.append((fila, col))
            for _ in range(eslora-1):
                if orientacion=="N": fila -= 1
                if orientacion=="S": fila += 1
                if orientacion=="E": col += 1
                if orientacion=="O": col -= 1
                barco.append((fila, col))
            if self.colocar_barco(barco):
                return True
        return False

    def inicializar_barcos(self):
        """Coloca todos los barcos de la biblioteca"""
        for nombre, eslora in self.barcos.items():
            colocado = False
            while not colocado:
                colocado = self.crear_barco_aleatorio(eslora)

    def recibir_disparo(self, coordenada):
        """Recibe un disparo y actualiza el tablero"""
        fila, col = coordenada
        if self.tablero_barcos[fila, col] == BARCO:
            self.tablero_barcos[fila, col] = TOCADO
            self.tablero_disparos[fila, col] = TOCADO
            return "Tocado"
        elif self.tablero_barcos[fila, col] == AGUA:
            self.tablero_disparos[fila, col] = AGUA_FALLADO
            return "Agua"
        else:
            return "Ya disparado aquí"

    def barcos_restantes(self):
        """Devuelve el número de casillas de barco sin tocar"""
        return np.sum(self.tablero_barcos == BARCO)