import numpy as np
from fractions import Fraction #Para que la solucion de la de en forma de fraccion

a1 = float(input("Cuanto vale a1: "))
b1 = float(input("Cuanto vale b1: "))
a2 = float(input("Cuanto vale a2: "))
b2 = float(input("Cuanto vale b2: "))
c1 = float(input("Cuanto vale c1: "))
c2 = float(input("Cuanto vale c2: "))

A = np.array([[a1, b1], [a2, b2]])
B = np.array([c1, c2])
#Lo dejaremos en funcion de incognitas ya que asi posteiromente se le puede pedir al usuario
#q las intruduzca o q se puda hacer de forma general

X = np.linalg.solve(A, B)
#solucion = round(X, 2) MAL EN ESTE CASO SI QIUERO REDONDEAR, LO TENGO QUE PONER DIRECTAMENTE EN LA SOL FINAL

#print(f"Solución: x = {round(X[0], 2)}, y = {round(X[1], 2)}")
#Las llaves sirven para meter una cadena de texto
#X[0] y X[1] sirve para indu¡icar las distintas soluciones que tiene X, en este caso 0 siendo la x y 1 la y
#Para redondear la solucion lo metemos directamente en el print que nos da la sol de la x y de la y


# Otra opcion de resultado es poner esta en fomra de graccion, para ello convierte los resultados a fracciones
x_frac = Fraction(X[0]).limit_denominator()
y_frac = Fraction(X[1]).limit_denominator()

# Imprime los valores de x e y como fracciones
print(f"Solución: x = {x_frac}, y = {y_frac}")