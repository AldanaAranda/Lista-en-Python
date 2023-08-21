oracion = input("Ingrese una frase: ")
letra = 0
for conteo in range(len(oracion)) :
    subcadena = oracion[conteo:conteo+1]
    if subcadena.isalpha() == True :
        letra += 1

print(f"Numero total de caracteres en la frase: {len(oracion)} con {letra} letras y {len(oracion.split())-1} espacios en blanco")