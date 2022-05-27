
def es_impar(numero):
    if numero % 2 == 0:
        return False

    else:
        return True

def main():
    var = int(input("Introduce un numero: "))
    print(es_impar(var))

if __name__ == '__main__':
    main()