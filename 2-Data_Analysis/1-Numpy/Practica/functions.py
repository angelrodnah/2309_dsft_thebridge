import numpy as np
import random

def crear_tablero(tamaño=(10,10)):
    return np.full(tamaño, " ")

def colocar_barco(barco, tablero):
    for casilla in barco:
        tablero[casilla] = "O"
    return tablero

def disparar(casilla, tablero):
    if tablero[casilla] == " ":
        print("Agua")
        tablero[casilla] = "-"
    else:
        print("Tocado")
        tablero[casilla] = "X"
    return tablero

def crear_barco_random(eslora):
    barco_random = []
    fila_random = random.randint(0,9)
    columna_random = random.randint(0,9)
    barco_random.append((fila_random, columna_random))

    # Oeste
    while len(barco_random) < eslora:
        columna_random = columna_random - 1
        barco_random.append((fila_random, columna_random))
    return barco_random
