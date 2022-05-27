
def fibonacci(numero):
    if numero == 0:
        return 0;

    elif numero == 1 or numero == 2:
        return 1;

    else:
        return fibonacci(numero - 2) + fibonacci(numero - 1)

def main():
    numero = int(input("Introduce el numero de fibonacci: "))
    print(fibonacci(numero))

if __name__ == '__main__':
    main()