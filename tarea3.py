import matplotlib.pyplot as plt

# Datos de ejemplo para altas y bajas
dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes"]
valores = [100, 120, 90, 130, 105]

# Crear la gráfica
plt.figure(figsize=(8, 5))
plt.plot(dias, valores, marker="o", color="b", linestyle="-", linewidth=2)

# Agregar flechas para mostrar altas y bajas
for i in range(1, len(valores)):
    if valores[i] > valores[i - 1]:  # Alta
        plt.annotate("", xy=(i, valores[i]), xytext=(i - 1, valores[i - 1]),
                     arrowprops=dict(arrowstyle="->", color="green", lw=2))
    elif valores[i] < valores[i - 1]:  # Baja
        plt.annotate("", xy=(i, valores[i]), xytext=(i - 1, valores[i - 1]),
                     arrowprops=dict(arrowstyle="->", color="red", lw=2))

# Configuración de la cuadrícula y etiquetas
plt.grid(True)
plt.title("Gráfica Estadística de Altas y Bajas")
plt.xlabel("Días")
plt.ylabel("Valores")
plt.show()
