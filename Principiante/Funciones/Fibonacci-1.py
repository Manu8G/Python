
def fibonacci(numero):
    aux = 0
    aux2 = 1
    lista = []
    lista.append(aux)
    lista.append(aux2)

    if numero != 0:
        for i in range(numero - 1):
            aux2 = aux2 + aux
            aux = lista[-1]
            lista.append(aux2)

        return aux2

    else:
        return 0

def main():
    numero = int(input("Introduce el numero de fibonacci: "))
    print(fibonacci(numero))

if __name__ == '__main__':
    main()