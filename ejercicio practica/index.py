def esPar(num) :
    if num % 2 == 0 :
        par = True
        return par

def multiplo(numer) :
    prueba = esPar(numer)
    if prueba == True and numer % 3 == 0 :
        esMultiplo = True
        return esMultiplo

def list(nume) :
    lista = []
    for i in range(nume) :
        compruebo = multiplo(i)
        if compruebo == True :
            lista.append(i)
    print(lista)

numero = int(input("Ingrese un numero "))

list(numero)