def esMultiplo(numero, valor3) :
    multiplo = False
    if numero % valor3 == 0 :
        multiplo = True
    return multiplo

print("Ingrese numeros enteros positivos")
A = int(input("Ingrese el primer valor: \n"))
B = int(input("Ingrese el segundo valor: \n"))
X = int(input("Ingrese el tercer valor: \n"))

if A > 0 and B > 0 and X > 0 :
    for lista in range(A, B+1) :
        numero = esMultiplo(lista, X)
        if numero == True :
            print(lista, end = ' ')
else :
    print("Lo siento, tenia que ingresar un numero entero positivo")