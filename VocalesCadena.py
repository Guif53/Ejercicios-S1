p = input("Dame una palabra: ") #no hace falta declarar q es string ya q siempre lo va a tomar asi

vocal = ["a","e","i","o","u"] #Como son texto hay q ponerlas entre comillas
contador = 0 #como queremos que nos cuente las vocales, tenemos que indicar que empieza en 0

for letra in p:
    if letra in vocal:
        contador += 1
    #elif letra 
        #input("No has metido una palabra, porfavor, introduzca una palabra: ")

print(contador)