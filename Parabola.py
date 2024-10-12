import matplotlib.pyplot as plt
import numpy as np

# Coeficientes de la ecuación cuadrática
a = 1
b = 0
c = 50

# Rango de valores de x
x = np.linspace(-10, 10, 500) #puede graficar 500 puntos entre el -10 y el 10 en el eje x

# Función cuadrática
y = a * x**2 + b * x + c

# Graficar la parábola
plt.plot(x, y, label=f'y = {a}x^2 + {b}x + {c}') #Crea el gráfico de la parábola con x en el eje horizontal y y en el eje vertical.
#La etiqueta label se usa para mostrar la ecuación en la leyenda del gráfico, y a lo q se iguala es a lo que quieras mostrar ahi, en este caso la ec cuadrática
plt.xlabel('x') #Añade la etiqueta a los ejes 
plt.ylabel('y')
plt.title('Gráfico de la función cuadrática') #pone el titulo a la gráfica
plt.legend() #Muestra la leyenda del gráfico, que incluye la ecuación de la parábola.
#Diferencia entre label y legend: Es como si label etiquetara las líneas y legend mostrara esas etiquetas en el gráfico para explicar qué es cada línea.
plt.grid(True) #Añade una cuadrícula al gráfico para facilitar la lectura.
plt.show()