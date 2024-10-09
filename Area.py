import numpy as np
r = int(input("Dime el radio de nuestra circunferencia: "))

while not (r >= 1):
    r = int(input("Ese nº no es entero, escriba un nº entero positivo entero: "))

operacion = float(np.pi * r**2)
resultado = round(operacion, 2)  # Redondear a 2 decimales
print(resultado)