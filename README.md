# Juego de la Vida – Versión Interactiva con Contador de Vecinos

Este programa implementa el **Juego de la Vida** de John Conway en Python, utilizando **NumPy** y **Matplotlib** para la simulación y visualización.

## 📜 Descripción

El Juego de la Vida es un **autómata celular** en el que cada celda de una cuadrícula puede estar en uno de dos estados: **viva (1)** o **muerta (0)**.  
En cada paso de tiempo, el estado de las celdas cambia según un conjunto de reglas basadas en el número de celdas vivas que tienen alrededor.

Este programa:

- Muestra la evolución del tablero en tiempo real.
- Presenta **dos gráficos**:
  1. El tablero actual (celdas vivas y muertas).
  2. El número de vecinos vivos que tiene cada celda.
- Incluye un **contador de celdas vivas**.
- Permite **pausar, reanudar y editar** el tablero durante la simulación.

---

## 📏 Reglas del Juego

1. **Supervivencia:** Una celda viva con **2 o 3** vecinos vivos sigue viva.
2. **Nacimiento:** Una celda muerta con **exactamente 3** vecinos vivos se convierte en viva.
3. **Muerte:**
   - Menos de 2 vecinos vivos → muere por soledad.
   - Más de 3 vecinos vivos → muere por sobrepoblación.

---

## 🖱 Controles

- **Barra espaciadora** → Pausar / reanudar la simulación.
- **Clic izquierdo sobre el tablero** (solo en pausa) → Alternar una celda entre viva y muerta.

---

## 📊 Elementos en pantalla

- **Panel izquierdo:** Representación en blanco y negro del tablero actual.
- **Texto superior izquierdo:** Contador de cuántas celdas están vivas.
- **Panel derecho:** Mapa de colores (`viridis`) que indica el número de vecinos vivos por celda.
  - Cada celda tiene un número dibujado con el conteo exacto.

---

## 🛠 Tecnologías usadas

- [NumPy](https://numpy.org/) → Manejo de la matriz del tablero y cálculo rápido de vecinos.
- [Matplotlib](https://matplotlib.org/) → Visualización del tablero y animación.

---

## Enlaces

- [Wikipedia](https://es.wikipedia.org/wiki/Juego_de_la_vida) → Enlace a wikipedia

## ▶ Ejecución

### 1️⃣ Instalar dependencias

```bash
pip install numpy matplotlib
