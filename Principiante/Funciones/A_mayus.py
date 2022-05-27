
def A_mayus(var):
    return ord(var) - 32

def main():
    cadena = list(input("Introduce una cadena de caracteres: "))
    for i in range(0, len(cadena)):
        if ord(cadena[i]) not in range(65, 90):
            cadena[i] = chr(A_mayus(cadena[i]))

    final = "".join([str(item) for item in cadena]) # Convierte la lista en string
    print(final)

if __name__ == '__main__':
    main()