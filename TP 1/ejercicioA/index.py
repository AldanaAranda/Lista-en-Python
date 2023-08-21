def Largo(num1, num2) :
    largo = 0
    if num1 > num2 :
        largo = num1
    else :
        largo = num2
    return largo

lado1 = int(input("Ingrese el valor del primer lado del rectangulo \n"))
lado2 = int(input("Ingrese el valor del segundo lado del rectangulo \n"))

largo = Largo(lado1, lado2)

if largo > 40 :
    print("Lo siento, el lado mas largo no puede superar los 40")
else :
    for i in range(lado2) :
        for j in range(lado1) :
            if i == 0 or i == lado2 - 1 or j == 0 or j == lado1 - 1:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()
