n = int(input("Escribe un nº entero positivo entero: "))

while not (n >= 1):
    n = int(input("Ese nº no es entero, escriba un nº entero positivo entero: "))
    
for num in range(1,n+1):
    print(num)