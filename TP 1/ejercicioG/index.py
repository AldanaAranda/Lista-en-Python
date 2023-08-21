oracion = input("Ingrese una frase: ")
cantidad = oracion.split()
mayor = 0
for conteo in range(len(cantidad)) :
    if len(cantidad[conteo]) > mayor :
        mayor = len(cantidad[conteo])
        posicion = conteo

print(f"La palabra mas larga es: {cantidad[posicion]}")