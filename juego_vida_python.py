import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Tamaño de la cuadrícula
ROWS = 30
COLS = 30

# Probabilidad inicial de que una celda esté viva
PROB_LIVE = 0.2

# Tiempo de actualización de la animación
UPDATE_INTERVAL = 100  # milisegundos

# Estado de pausa
paused = False


# Aquí creo una matriz inicial con celdas vivas o muertas
def crear_tablero(rows, cols, prob_live):
    return np.random.choice([0, 1], size=(rows, cols), p=[1 - prob_live, prob_live])


# Con esta función cuento los vecinos vivos de una celda y los agrego a un array
# que se usará para mostrar el número de vecinos en la segunda subgráfica.
def contar_vecinos(tablero, x, y):
    filas, cols = tablero.shape
    count = 0
    for dx in (-1, 0, 1):
        for dy in (-1, 0, 1):
            if dx == 0 and dy == 0:
                continue
            nx = (x + dx) % filas
            ny = (y + dy) % cols
            count += tablero[nx, ny]
    return count

# Con esta función creo un array que contiene el número de vecinos vivos para cada celda
# y lo uso para mostrarlo en la segunda subgráfica.
def crear_array_vecinos(tablero):
    vecinos_array = np.zeros((ROWS, COLS), dtype=int)
    for i in range(ROWS):
        for j in range(COLS):
            vecinos_array[i, j] = contar_vecinos(tablero, i, j)
    return vecinos_array


# Esta función calcula la siguiente generación del tablero según las reglas del juego
# de la vida de Conway.
def siguiente_generacion(tablero):
    new_tablero = np.copy(tablero)
    for i in range(tablero.shape[0]):
        for j in range(tablero.shape[1]):
            vecinos_vivos = contar_vecinos(tablero, i, j)
            if tablero[i, j] == 1:
                if vecinos_vivos < 2 or vecinos_vivos > 3:
                    new_tablero[i, j] = 0
            else:
                if vecinos_vivos == 3:
                    new_tablero[i, j] = 1
    return new_tablero


# --- Animación ---
tablero = crear_tablero(ROWS, COLS, PROB_LIVE)

fig, axes = plt.subplots(1, 2, figsize=(8, 4))

# Subplot 1: tablero
img_tablero = axes[0].imshow(tablero, interpolation='nearest', cmap="binary")
axes[0].set_title("Juego de la Vida")
axes[0].axis('off')

# Texto para mostrar el número de vivas
contador_texto = axes[0].text(
    0, -2, "", fontsize=10, color="black", ha="left", va="center"
)

# Subplot 2: vecinos
vecinos = crear_array_vecinos(tablero)
img_vecinos = axes[1].imshow(vecinos, interpolation='nearest', cmap="viridis")
axes[1].set_title("Número de vecinos")
textos_vecinos = []
for i in range(ROWS):
    fila_textos = []
    for j in range(COLS):
        txt = axes[1].text(j, i, str(vecinos[i, j]), ha='center', va='center', color='white')
        fila_textos.append(txt)
    textos_vecinos.append(fila_textos)
axes[1].axis('off')


# Función de actualización de la animación
def actualizar(frameNum):
    global tablero
    if not paused:
        tablero[:] = siguiente_generacion(tablero)
    img_tablero.set_data(tablero)

    # Contador de celdas vivas
    celdas_vivas = np.sum(tablero)
    contador_texto.set_text(f"Celdas vivas: {celdas_vivas}")

    nuevos_vecinos = crear_array_vecinos(tablero)
    img_vecinos.set_data(nuevos_vecinos)

    for i in range(ROWS):
        for j in range(COLS):
            textos_vecinos[i][j].set_text(str(nuevos_vecinos[i, j]))

    return img_tablero, img_vecinos, contador_texto

# Funciones para manejar eventos de teclado y clics del ratón
def on_key(event):
    global paused
    if event.key == ' ':
        paused = not paused


def on_click(event):
    global tablero
    if paused and event.inaxes == axes[0]:
        col = int(round(event.xdata))
        row = int(round(event.ydata))
        if 0 <= row < ROWS and 0 <= col < COLS:
            tablero[row, col] = 1 - tablero[row, col]
            actualizar(None)
            fig.canvas.draw_idle()


fig.canvas.mpl_connect('key_press_event', on_key)
fig.canvas.mpl_connect('button_press_event', on_click)

fig.ani = animation.FuncAnimation(fig, actualizar, frames=100, interval=UPDATE_INTERVAL, blit=False)
plt.show()
