texto = input("Ingrese una frase: ")
vocal = 0
for conteo in range(len(texto)) :
    textoMayuscula = texto.upper()
    if textoMayuscula[conteo:conteo+1] == 'A' or textoMayuscula[conteo:conteo+1] == 'E' or textoMayuscula[conteo:conteo+1] == 'I'or textoMayuscula[conteo:conteo+1] == 'O' or textoMayuscula[conteo:conteo+1] == 'U':
        vocal += 1
print(f"Total de vocales: {vocal}")