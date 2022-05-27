
def suma(lista):
    solucion = 0
    for i in lista:
        solucion += i

    return solucion

def main():
    var = int(input("Introduce un valor (-1 para salir): "))
    lista = []

    while var != -1:
        lista.append(var)
        var = int(input("Introduce un valor (-1 para salir): "))

    print(suma(lista))

if __name__ == '__main__':
    main()