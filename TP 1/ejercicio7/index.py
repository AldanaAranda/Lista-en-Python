def esPar(num) :
    if num % 2 == 0 :
        par = True
        return par

numero = int(input("Ingrese un numero entero positivo \n"))

print("Contemos!")

for conteo in range(2, numero+1) :
    par = esPar(conteo)
    if par == True :
        print(conteo, end = ' ')

