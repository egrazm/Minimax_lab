import random
from constantes import TURNOS_MAX, MOVIMIENTOS  # Constantes: máximo de turnos y posibles movimientos
from tablero import crear_tablero, mostrar_tablero, posicion_aleatoria, son_adyacentes, anadir_obstaculos, cantidad
from movimiento import mover_personaje, N  # Función para mover personajes y tamaño del tablero
from minimax import mover_minimax  # Lógica del movimiento inteligente (Minimax)
from tablero import colocar_queso  # Para colocar bloques de queso en el tablero

def jugar():
    # El jugador elige si quiere controlar al gato o al ratón
    eleccion = input("Elegí 😺 o 🐭 (gato o ratón): ").strip().lower()

    # Se crea el tablero vacío y se añaden obstáculos
    tablero = crear_tablero()
    anadir_obstaculos(tablero, cantidad)

    # Se colocan bloques de queso en el tablero
    cantidad_queso = int(N / 2)  # Cantidad de quesos según el tamaño del tablero
    colocar_queso(tablero, cantidad_queso)
    queso_recogido = 0  # Contador del queso que ha recogido el ratón

    # Se generan posiciones aleatorias para el gato y el ratón que no estén juntas
    while True:
        raton_pos = posicion_aleatoria()
        gato_pos = posicion_aleatoria()
        if not son_adyacentes(raton_pos, gato_pos):
            break

    # Se colocan los personajes en el tablero
    tablero[raton_pos[0]][raton_pos[1]] = "🐭"
    tablero[gato_pos[0]][gato_pos[1]] = "🐱"

    turnos = TURNOS_MAX  # Número total de turnos disponibles
    turno_actual = 1
    ulti_gat = []  # Historial del movimiento anterior del gato (para evitar ciclos)
    ulti_rat = []  # Historial del movimiento anterior del ratón

    # Bucle principal del juego
    while turnos > 0:
        print(f"\nTurnos restantes: {turnos}")
        mostrar_tablero(tablero)

        # Turno del jugador
        if eleccion == "raton":
            mov = input("Movimiento del 🐭 (w/a/s/d): ").lower()
            if mov not in MOVIMIENTOS:
                print("❌ Movimiento inválido. Usa solo w/a/s/d.")
                continue

            # Mueve el ratón, actualiza la posición y recoge queso si lo pisa
            raton_pos, recogio_queso = mover_personaje(tablero, raton_pos, mov, "🐭", ulti_rat)
            if recogio_queso:
                queso_recogido += 1

            # Movimiento inteligente del gato con minimax
            gato_pos_nueva = mover_minimax(tablero, gato_pos, True, gato_pos, raton_pos, ulti_gat[-1] if ulti_gat else None)
            ulti_gat.append(gato_pos)
            if len(ulti_gat) > 1:
                ulti_gat.pop(0)
            gato_pos = gato_pos_nueva

        else:  # Si el jugador eligió al gato
            mov = input("Movimiento del 🐱 (w/a/s/d): ").lower()
            if mov not in MOVIMIENTOS:
                print("❌ Movimiento inválido. Usa solo w/a/s/d.")
                continue

            dx, dy = MOVIMIENTOS[mov]
            nueva_pos = (gato_pos[0] + dx, gato_pos[1] + dy)

            # Verifica que la nueva posición sea válida
            if not (0 <= nueva_pos[0] < N and 0 <= nueva_pos[1] < N):
                print("❌ Movimiento fuera del tablero.")
                continue

            # El gato no puede caminar sobre queso
            if tablero[nueva_pos[0]][nueva_pos[1]] == "🧀":
                print("❌ El gato no puede moverse sobre el queso.")
                continue

            # Movimiento válido del gato
            gato_pos, _ = mover_personaje(tablero, gato_pos, mov, "🐱", ulti_gat)
            if len(ulti_gat) > 1:
                ulti_gat.pop(0)

            # Movimiento del ratón: aleatorio en los primeros 2 turnos, luego usa minimax
            if turno_actual <= 2:
                dx, dy = random.choice(list(MOVIMIENTOS.values()))
                nueva_pos = (raton_pos[0] + dx, raton_pos[1] + dy)
                if 0 <= nueva_pos[0] < N and 0 <= nueva_pos[1] < N:
                    tablero[raton_pos[0]][raton_pos[1]] = "🌿"
                    raton_pos = nueva_pos
                    tablero[raton_pos[0]][raton_pos[1]] = "🐭"
            else:
                raton_pos_nueva = mover_minimax(tablero, raton_pos, False, gato_pos, raton_pos, ulti_rat[-1] if ulti_rat else None)
                ulti_rat.append(raton_pos)
                if len(ulti_rat) > 1:
                    ulti_rat.pop(0)
                raton_pos = raton_pos_nueva

        # Verifica si el gato atrapó al ratón
        if gato_pos == raton_pos:
            tablero[gato_pos[0]][gato_pos[1]] = "💥"
            mostrar_tablero(tablero)
            print("💥 ¡El gato atrapó al ratón! Fin del juego.")
            return

        turnos -= 1
        turno_actual += 1

    # Condición final: el ratón escapa, se verifica si cumplió su misión
    if queso_recogido >= cantidad_queso:
        print("🐭 ¡El ratón recogió todo el queso y escapó exitosamente!")
    else:
        print(f"❌ El ratón escapó, pero solo recolectó {queso_recogido}/{cantidad_queso} quesos.")
        print("💀 ¡No cumplió su misión!")

# Ejecuta el juego si el archivo se corre directamente
if __name__ == "__main__":
    jugar()