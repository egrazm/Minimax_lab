# 🐱 Laberinto del Gato y el Ratón 🐭

Una simulación interactiva de persecución entre un gato y un ratón en un **laboratorio subterráneo**.  
El jugador elige controlar a uno de los dos personajes, con objetivos distintos. El entorno está lleno de **queso**, **trampas** y obstáculos, y la inteligencia artificial del oponente está basada en el algoritmo **Minimax**.

---

## 🎯 Objetivos del Juego

- 🐭 **Ratón** (jugador o IA): debe recolectar queso y escapar antes de que se agoten los turnos.
- 🐱 **Gato** (jugador o IA): debe atrapar al ratón antes de que logre escapar o pasen los turnos.

---

## ⚙️ Características

- 🔲 Tablero de tamaño configurable con diseño visual usando **emojis**.
- 🎮 Movimiento por teclado con las teclas `w`, `a`, `s`, `d`.
- 🧠 Implementación del algoritmo **Minimax** para decisiones inteligentes.
- 🎲 Comportamiento inicial aleatorio del ratón (si el jugador controla al gato).
- ⏳ Sistema de **turnos limitados**.
- 🪤 Obstáculos y trampas colocados en el mapa.
- 🧀 Bloques de queso recolectables por el ratón.
- 📁 Código estructurado en **módulos** para mantener claridad y escalabilidad.

---

## ✔️ Lo que funcionó bien

- ✅ Estética clara del tablero con **emojis** y buena legibilidad.
- ✅ IA funcional y estratégica para ambos personajes usando Minimax.
- ✅ Separación efectiva de la lógica del juego en módulos:
  - `tablero.py`
  - `minimax.py`
  - `movimiento.py`
- ✅ Controles simples e intuitivos (`w/a/s/d`).

---

## 💥 Desafíos superados

- ⚠️ Dificultades al modularizar el código sin romper funcionalidad.
- ⚠️ Primeras versiones de Minimax generaban decisiones erráticas o lentas.
- ⚠️ Problemas con la representación visual: algunos movimientos no se reflejaban correctamente.
- ⚠️ La introducción de obstáculos causó errores en la lógica y desorden visual.

---

## 💡 Mejores momentos del desarrollo

- 🎨 Incorporación de visuales con emojis que dieron vida al juego.
- 🧠 Comprensión profunda del algoritmo Minimax, ajustando su profundidad para lograr decisiones más eficientes.

