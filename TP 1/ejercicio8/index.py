valores = int(input("Ingrese cuantos valores quiere ingresar \n"))
suma = 0
for lista in range(valores) :
    numero = float(input("Ingrese un valor: \n"))
    suma += numero

print(f"La suma de los valores ingresados es: {suma}")
print(f"El promedio de los valores ingresados es: {suma / valores}")