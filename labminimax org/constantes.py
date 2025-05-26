
from tablero import eleccion
if eleccion =="p":
    TURNOS_MAX=12
elif eleccion=="m":
    TURNOS_MAX=25
elif eleccion=="g":
    TURNOS_MAX=30




MOVIMIENTOS = {
    "w": (-1, 0),  # arriba
    "s": (1, 0),   # abajo
    "a": (0, -1),  # izquierda
    "d": (0, 1),   # derecha
}