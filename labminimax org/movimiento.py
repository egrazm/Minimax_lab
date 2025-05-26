from constantes import MOVIMIENTOS
from tablero import N

def mover_personaje(tablero, pos_actual, direccion, emoji, ulti):
    dx, dy = MOVIMIENTOS.get(direccion, (0, 0))
    nueva_pos = (pos_actual[0] + dx, pos_actual[1] + dy)
    recogio_queso = False

    if 0 <= nueva_pos[0] < N and 0 <= nueva_pos[1] < N:
        destino = tablero[nueva_pos[0]][nueva_pos[1]]
        if destino == "🪤":
            print("🚫 Hay un obstáculo en esa dirección.")
            return pos_actual, False

        if emoji == "🐭" and destino == "🧀":
            print("🧀 ¡Has recogido un trozo de queso!")
            recogio_queso = True

        tablero[pos_actual[0]][pos_actual[1]] = "🌿"
        tablero[nueva_pos[0]][nueva_pos[1]] = emoji
        ulti.append(pos_actual)
        if len(ulti) > 4:
            ulti.pop(0)

        return nueva_pos, recogio_queso

    print("🚫 Movimiento inválido (fuera del tablero).")
    return pos_actual, False
