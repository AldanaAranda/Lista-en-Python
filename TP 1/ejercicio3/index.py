def calcular(Ancho, Largo, Alto, Manos) :
    paredAyB = Ancho * Largo * 2
    paredCyD = Largo * Alto * 2
    totalParedes = paredAyB + paredCyD
    totalPintura = (totalParedes - (0.8 * 2)) / 10
    totalPintura *= Manos

    return totalPintura

ancho = float(input("Ingrese el valor del ancho: "))
largo = float(input("Ingrese el valor del largo: "))
alto = float(input ("Ingrese el valor del alto: "))
mano = float(input("Cuantas manos de pinturas? "))

cantPintura = calcular(ancho, largo, alto, mano)

print(f"Se necesitan {cantPintura} litros de pintura para pintar la habitacion")