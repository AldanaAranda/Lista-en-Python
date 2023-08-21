numero = int(input("Ingrese un numero entero positivo \n"))
if numero >= 0 :
    if numero == 0 :
        print("0")
    print("Contemos!")
    for conteo in range(1, numero+1) :
        print(conteo, end = ' ')
else :
    print("Lo siento, tenia que ingresar un numero entero positivo")