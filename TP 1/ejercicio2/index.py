def calcular(Ancho, Largo, Alto) :
    paredAyB = Ancho * Largo * 2
    paredCyD = Largo * Alto * 2
    totalParedes = paredAyB + paredCyD
    totalPintura = (totalParedes - (0.8 * 2)) / 10

    return totalPintura

ancho = float(input("Ingrese el valor del ancho: "))
largo = float(input("Ingrese el valor del largo: "))
alto = float(input ("Ingrese el valor del alto: "))

cantPintura = calcular(ancho, largo, alto)

print(f"Se necesitan {cantPintura} litros de pintura para pintar la habitacion")