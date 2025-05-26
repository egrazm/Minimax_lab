import random
from random import randint

eleccion = str(input("Elija una opcion de tablero(P,M,G): ")).strip().lower()  # Tamaño del tablero

if eleccion =="p":
    N=4
    cantidad=3
elif eleccion=="m":
    N=6
    cantidad=6
elif eleccion=="g":
    N=8
    cantidad=12
else:
    print("Opcion no valida")


def crear_tablero():
    return [["🌿" for _ in range(N)] for _ in range(N)]

def mostrar_tablero(tablero):
    for fila in tablero:
        print(" ".join(fila))

def posicion_aleatoria():
    return (random.randint(0, N - 1), random.randint(0, N - 1))

def son_adyacentes(pos1, pos2):
    return max(abs(pos1[0] - pos2[0]), abs(pos1[1] - pos2[1])) <= 1

def anadir_obstaculos(tablero, cantidad):
    colocados = 0
    ocupados = set()
    while colocados < cantidad:
        fila, col = posicion_aleatoria()
        if tablero[fila][col] == "🌿":
            tablero[fila][col] = "🪤"
            ocupados.add((fila, col))
            colocados += 1


def colocar_queso(tablero, cantidad_queso):
    queso_colocados = 0
    while queso_colocados < cantidad_queso:
        x, y = randint(0, len(tablero)-1), randint(0, len(tablero[0])-1)
        if tablero[x][y] == "🌿": 
            tablero[x][y] = "🧀"
            queso_colocados += 1