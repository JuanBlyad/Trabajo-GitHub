import numpy as np
import matplotlib.pyplot as plt

# 1. Crear un vector de tamaño 720 con valores aleatorios
vector = np.random.rand(720)

# 2. Hacer reshape a (120, 6)
matriz = vector.reshape(120, 6)

# 3. Hacer la transpuesta de la matriz y crear dos copias, una usando order 'F' y otra usando order 'C'
matriz_T = matriz.T
matriz_F = np.asfortranarray(matriz_T)
matriz_C = np.ascontiguousarray(matriz_T)

# 4. Establecer estilo y crear una figura
plt.style.use('seaborn-white')
fig = plt.figure(figsize=(15, 10))

# 5. Crear 6 subplots "a mano" con proporciones diferentes
# Panel 1: Plot
ax1 = plt.axes([0.05, 0.55, 0.25, 0.35])  # posición [left, bottom, width, height]
ax1.plot(matriz_F[0])
ax1.set_title('Plot')
ax1.set_xlabel('X')
ax1.set_ylabel('Y')
ax1.grid(True)

# Panel 2: Scatter
ax2 = plt.axes([0.35, 0.55, 0.25, 0.35])
ax2.scatter(range(len(matriz_F[1])), matriz_F[1])
ax2.set_title('Scatter')
ax2.set_xlabel('X')
ax2.set_ylabel('Y')
ax2.grid(True)

# Panel 3: Bar
ax3 = plt.axes([0.65, 0.55, 0.25, 0.35])
ax3.bar(range(len(matriz_F[2])), matriz_F[2])
ax3.set_title('Bar')
ax3.set_xlabel('X')
ax3.set_ylabel('Y')
ax3.grid(True)

# Panel 4: Histograma
ax4 = plt.axes([0.05, 0.1, 0.25, 0.35])
ax4.hist(matriz_F[3])
ax4.set_title('Histograma')
ax4.set_xlabel('X')
ax4.set_ylabel('Y')
ax4.grid(True)

# Panel 5: Pie
ax5 = plt.axes([0.35, 0.1, 0.25, 0.35])
ax5.pie(matriz_F[4], labels=range(len(matriz_F[4])), autopct='%1.1f%%')
ax5.set_title('Pie')

# Panel 6: Boxplot
ax6 = plt.axes([0.65, 0.1, 0.25, 0.35])
ax6.boxplot(matriz_F[5])
ax6.set_title('Boxplot')
ax6.set_xlabel('X')
ax6.set_ylabel('Y')
ax6.grid(True)

# 6. Ajustar el diseño
plt.tight_layout()
plt.show()
