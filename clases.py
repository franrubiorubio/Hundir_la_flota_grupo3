import numpy as np
import random
from variables import lista_barcos
#TABLERO

class Tablero :
    def __init__(self , id_jugador, filas=10, columnas=10 , agua="~"):
        self.filas = filas
        self.columnas = columnas
        self.id_jugador = id_jugador
        self.agua = agua
        self.crear_tablero()  # lo creamos directamente al iniciar
        self.vidas = 20 


    def crear_tablero(self):
        self.tablero = np.full((self.filas, self.columnas), self.agua)
        self.tablero_jugador= np.full((self.filas,self.columnas), self.agua)
        self.tablero_mascara_jugador = np.full((self.filas, self.columnas), self.agua)
        self.tablero_mascara_maquina = np.full((self.filas, self.columnas), self.agua)
        return self.tablero
    
    def coloca_barco(self, barco):# verifica que se puede poner el barco en el tablero
        
        tablero_temp = self.tablero.copy()

        for fila, columna in barco:
            if fila < 0 or fila >= self.filas or columna < 0 or columna >= self.columnas:
                return False
            
            if self.tablero[fila, columna] == "O":  
                return False

            tablero_temp[fila, columna] = "O"

        self.tablero = tablero_temp  
        return self.tablero


    def recibir_disparos_maquina(self, tablero ):  #dispara la maquina
        fila = random.randint(0, self.filas - 1)
        columna = random.randint(0, self.columnas - 1)

        if tablero.tablero[fila, columna] == "O":
            tablero.tablero_jugador[fila, columna] = "X"
            self.vidas -= 1 
            print(f"Tocado en {(fila, columna)} \nAl jugador le quedan {self.vidas} vidas\n", tablero.tablero_jugador)
            return True  # vuelve a tirar
            
        elif tablero.tablero[fila, columna] == "~":
            tablero.tablero_jugador[fila, columna] = "|"
            print(f"Agua en {(fila, columna)}\n", tablero.tablero_jugador)
            return False  # cambia turno

        else:
            print(f"Ya has disparado en {(fila, columna)}\n", tablero.tablero_jugador)
            return False


        

    def recibir_disparo(self, tablero):  #dispara el jugador
        fila = int(input("Dime la fila: "))
        columna = int(input("Dime la columna: "))

        if tablero.tablero[fila, columna] == "O":
            tablero.tablero_mascara_maquina[fila, columna] = "X"
            self.vidas -= 1
            print(f"Tocado en {(fila, columna)} \nA la máquina le quedan {self.vidas} vidas\n", tablero.tablero_mascara_maquina)
            return True  # vuelve a disparar

        elif tablero.tablero[fila, columna] == self.agua:
            tablero.tablero_mascara_maquina[fila, columna] = "|"
            print("Agua\n", tablero.tablero_mascara_maquina)
            return False  # cambia turno

        else:
            print("Ya has disparado aquí\n", tablero.tablero_mascara_maquina)
            return False
        


tablero_jugador = Tablero("jugador")
tablero_maquina = Tablero("maquina")
#BARCO
class Barco:

    def __init__(self, nombre, eslora, id_jugador):
        self.nombre = nombre
        self.eslora = eslora
        self.id_jugador = id_jugador

    def crea_barco_aleatorio(self, tablero, num_intentos=100):
        

        for intento in range(num_intentos):

            barco = []

            fila_ini = random.randint(0, tablero.filas - 1)
            col_ini = random.randint(0, tablero.columnas - 1)

            orientacion = random.choice(["N", "S", "E", "W"])
            fila, col = fila_ini, col_ini

            barco.append((fila, col))
#el random elige la direccion del barco 
            for _ in range(self.eslora - 1):

                if orientacion == "N":
                    fila -= 1
                elif orientacion == "S":
                    fila += 1
                elif orientacion == "E":
                    col += 1
                elif orientacion == "W":
                    col -= 1

                barco.append((fila, col))

            # Intentamos colocarlo
            resultado = tablero.coloca_barco(barco)

            if isinstance(resultado, np.ndarray):
                #print(f"Barco {self.nombre} colocado en:", barco)
                return barco

        #print("No se pudo colocar el barco tras muchos intentos.")
        return False

#estos for ubica los barcos en los tableros
for nombre, tamaño in lista_barcos.items():
    barco = Barco(nombre, tamaño, "jugador")
    barco.crea_barco_aleatorio(tablero_jugador)
    crear_barco_jugador = tablero_jugador.tablero


for nombre, tamaño in lista_barcos.items():
    barco = Barco(nombre, tamaño, "maquina")
    barco.crea_barco_aleatorio(tablero_maquina)