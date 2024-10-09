nombrep = input("Dame un nombre: ")
añop = int(input("Dime que año nacio: "))
alturap = float(input("Dime cuantos cemtímetros mide: "))

class Persona:
    def __init__(self, nombre, año, altura):
        self.nombre = nombre
        self.año = año
        self.edad = 2024-año
        self.altura = altura

    def saludar(self):
        print(f"Hola, me llamo {self.nombre} y tengo {self.edad} años y mido {self.altura} cm.")

persona1 = Persona(nombrep, añop, alturap)
persona1.saludar()