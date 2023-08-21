def esEquilatero(numero1, numero2, numero3) :
    Equilatero = False
    if num1 == num2 and num2 == num3 :
        Equilatero = True
    return Equilatero

def esIsosceles(numero1, numero2, numero3) :
    Isosceles = False
    if numero1 == numero2 or numero1 == numero3 or numero2 == numero3 :
        Isosceles = True
    return Isosceles

def resultado(nume1, nume2, nume3) :
    equilatero = esEquilatero(nume1, nume2, nume3)
    isosceles = esIsosceles(nume1, nume2, nume3)
    if nume1 != 0 and nume2 != 0 and nume3 != 0 :
        if equilatero == True :
            print("Es un triangulo equilatero")
        elif isosceles == True :
            print("Es un triangulo isosceles")
        else  :
            print("Es un triangulo escaleno")
    else :
        print("El valor del lado tiene que ser distinto de cero")


num1 = float(input("Ingrese el valor del lado 1 "))
num2 = float(input("Ingrese el valor del lado 2 "))
num3 = float(input("Ingrese el valor del lado 3 "))

resultado(num1, num2, num3)