
def potencia(numero, exponente=2):
    return numero ** exponente

def main():
    valor = int(input("Introduce un numero: "))
    var = input("Quieres introducir su potencia(S/N): ")

    if var == "S":
        num = int(input("Introduce la potencia que quieras: "))
        # print(potencia(valor, exponente=num))
        print(potencia(valor, num)) # Tambien vale lo de arriba
    else:
        print(potencia(valor))

if __name__ == '__main__':
    main()