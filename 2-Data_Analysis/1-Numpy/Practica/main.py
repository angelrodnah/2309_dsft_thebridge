from functions import *

tablero = crear_tablero()

barco_1 = [(0,1), (1,1)]
barco_2 = [(1,3), (1,4), (1,5), (1,6)]
barco_3 = crear_barco_random(3)

tablero = colocar_barco(barco_1, tablero)
tablero = colocar_barco(barco_2, tablero)
tablero = colocar_barco(barco_3, tablero)

print(tablero)

tablero = disparar((1,1), tablero)
print(tablero)

tablero = disparar((2,1), tablero)
print(tablero)