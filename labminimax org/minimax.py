from constantes import MOVIMIENTOS
from tablero import N

#Calculo de la distancia Manhattan entre el gato y el raton
def evaluar_estado(gato_pos, raton_pos):
    return abs(gato_pos[0] - raton_pos[0]) + abs(gato_pos[1] - raton_pos[1])

#Funcion de tomar la decision optima para el gato y el raton, simundo mov futuros con profundidad
def minimax(gato_pos, raton_pos, es_turno_gato, profundidad, tablero, ulti):
    if profundidad == 0 or gato_pos == raton_pos:
        return evaluar_estado(gato_pos, raton_pos), None

    mejor_valor = float('inf') if es_turno_gato else float('-inf')
    mejor_mov = None

    for dx, dy in MOVIMIENTOS.values():
        if es_turno_gato:
            nueva_pos = (gato_pos[0] + dx, gato_pos[1] + dy)
        else:
            nueva_pos = (raton_pos[0] + dx, raton_pos[1] + dy)

        # Validar que se mantenga dentro del tablero y sin trampas
        if (
            0 <= nueva_pos[0] < N and 0 <= nueva_pos[1] < N and
            tablero[nueva_pos[0]][nueva_pos[1]] != "🪤" and
            (not es_turno_gato or tablero [nueva_pos[0]][nueva_pos[1]]!="🧀")
        ):
            # Evitar repetir el último movimiento del ratón
            if ulti and not es_turno_gato and nueva_pos == ulti:
                continue

            if es_turno_gato:
                val, _ = minimax(nueva_pos, raton_pos, False, profundidad - 1, tablero, ulti)
                if val < mejor_valor:
                    mejor_valor = val
                    mejor_mov = (dx, dy)
            else:
                val, _ = minimax(gato_pos, nueva_pos, True, profundidad - 1, tablero, ulti)
                if val > mejor_valor:
                    mejor_valor = val
                    mejor_mov = (dx, dy)

    return mejor_valor, mejor_mov

def mover_minimax(tablero, pos, es_gato, gato_pos, raton_pos, ulti):
    _, mov = minimax(gato_pos, raton_pos, es_gato, 3, tablero, ulti)

    if mov:
        dx, dy = mov
        nueva_pos = (pos[0] + dx, pos[1] + dy)

        if (
            0 <= nueva_pos[0] < N and 0 <= nueva_pos[1] < N and
            tablero[nueva_pos[0]][nueva_pos[1]] != "🪤" and
            (not es_gato or tablero[nueva_pos[0]][nueva_pos[1]] != "🧀")
        ):
            tablero[pos[0]][pos[1]] = "🌿"
            emoji = "🐱" if es_gato else "🐭"
            tablero[nueva_pos[0]][nueva_pos[1]] = emoji
            return nueva_pos

    return pos
