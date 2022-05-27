
def Adivinar(var):
    numero = int(input("Introduce numeros hasta que lo adivines: "))
    while numero != var:
        numero = int(input())


def main():
    numero = 5
    Adivinar(numero)
    print("Lo has adivinado!!")

if __name__ == '__main__':
    main()