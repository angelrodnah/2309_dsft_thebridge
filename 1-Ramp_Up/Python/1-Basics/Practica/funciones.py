import math

def calculadora_radianes():
    grados = float(input("Introduzca los grados").replace(',','.'))

    radianes = grados * (math.pi/180)
    print("Los radianes son", radianes)

a = 1