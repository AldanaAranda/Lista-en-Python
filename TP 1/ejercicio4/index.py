mayor = 0
for vueltas in range(3) :
    numero = int(input("Ingrese un numero:  "))
    if numero > mayor :
        mayor = numero

print(f"El numero mas grande es {mayor}")