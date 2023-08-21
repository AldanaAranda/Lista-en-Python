suma = 0
contador = 0
numero = int(input("Ingrese un numero \n"))

if numero <= 0 :
    print("El promedio es: 0 con un total de 0 ingresos")
else :
    while numero > 0 :
        suma += numero
        numero = int(input("Ingrese otro numero \n"))
        contador += 1
    print(f"El promedio es: {suma/contador} con un total de {contador} ingresos")
